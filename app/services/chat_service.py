from app.core.config import settings
from app.models.chat import ChatRequest, ChatMessage
from openai import OpenAI


class ChatService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    async def generate_chat_response(self, request: ChatRequest):
        # Construir la lista de mensajes para OpenAI
        messages = [
            {"role": "system",
             "content": "Eres un experto en gestión de proyectos y certificación PMP. Mantienes el contexto de la conversación y puedes referirte a información mencionada previamente por el usuario."}
        ]

        # Agregar el historial de mensajes
        messages.extend([
            {"role": msg.role, "content": msg.content}
            for msg in request.message_history
        ])

        # Agregar el mensaje actual
        messages.append({"role": "user", "content": request.message})

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )

        return {
            "response": response.choices[0].message.content,
            "usage": {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            }
        }


chat_service = ChatService()