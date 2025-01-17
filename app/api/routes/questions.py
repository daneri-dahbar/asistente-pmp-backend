from fastapi import APIRouter, Query
from app.models.response import QuestionResponse
from app.models.domain import Domain
from app.services.openai_service import openai_service

router = APIRouter()

@router.get("/question", response_model=QuestionResponse)
async def get_pmp_question(
    domain: Domain = Query(
        ...,
        description="Dominio de la pregunta PMP: personas, proceso o entorno"
    )
):
    try:
        question = await openai_service.get_single_question(domain)
        return QuestionResponse(success=True, data=question)
    except Exception as e:
        return QuestionResponse(success=False, error=str(e))