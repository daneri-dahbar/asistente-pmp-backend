from fastapi import APIRouter, HTTPException, Header, status
from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import chat_service
from app.services.auth_service import auth_service
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_model=ChatResponse)
async def chat_with_gpt(
        request: ChatRequest,
        authorization: str = Header(None)
):
    """
    Endpoint para chatear con GPT-4.
    Requiere autenticación via Bearer token.
    """
    try:
        logger.info("Recibiendo solicitud de chat")

        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token de autenticación no proporcionado o formato inválido"
            )

        token = authorization.split("Bearer ")[1]
        user = await auth_service.get_current_user(token)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido o expirado"
            )

        logger.info(f"Usuario autenticado: {user.email}")
        logger.info(f"Mensaje recibido: {request.message}")

        try:
            response = await chat_service.generate_chat_response(request)
            logger.info("Respuesta generada exitosamente")
            return ChatResponse(**response)
        except Exception as e:
            logger.error(f"Error al generar respuesta: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al generar respuesta: {str(e)}"
            )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado: {str(e)}"
        )