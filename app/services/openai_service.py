from openai import OpenAI
from typing import Optional
from app.core.config import settings
from app.core.constants import get_question_prompt
from app.models.question import Question, Option
from app.models.domain import Domain


class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    async def _process_question_block(self, block: str, domain: Domain) -> Optional[Question]:
        lines = block.strip().split('\n')
        question_text = None
        options = []
        correct_answer = None
        explanation = None

        for line in lines:
            line = line.strip()
            if line.startswith('PREGUNTA:'):
                question_text = line.replace('PREGUNTA:', '').strip()
            elif line.startswith('A)'):
                options.append(Option(text=line[2:].strip(), is_correct=False))
            elif line.startswith('B)'):
                options.append(Option(text=line[2:].strip(), is_correct=False))
            elif line.startswith('C)'):
                options.append(Option(text=line[2:].strip(), is_correct=False))
            elif line.startswith('D)'):
                options.append(Option(text=line[2:].strip(), is_correct=False))
            elif line.startswith('RESPUESTA CORRECTA:'):
                correct_answer = line.replace('RESPUESTA CORRECTA:', '').strip()
            elif line.startswith('EXPLICACIÓN:'):
                explanation = line.replace('EXPLICACIÓN:', '').strip()

        if question_text and len(options) == 4 and correct_answer and explanation:
            correct_index = ord(correct_answer) - ord('A')
            if 0 <= correct_index < len(options):
                options[correct_index].is_correct = True
                return Question(
                    question_text=question_text,
                    options=options,
                    explanation=explanation,
                    domain=domain
                )
        return None

    async def get_single_question(self, domain: Domain) -> Question:
        prompt = get_question_prompt(domain.value)

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un experto en gestión de proyectos y certificación PMP."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )

        content = response.choices[0].message.content
        question = await self._process_question_block(content, domain)
        if not question:
            raise ValueError("No se pudo procesar la pregunta correctamente")
        return question


openai_service = OpenAIService()