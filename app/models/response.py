from typing import Optional
from pydantic import BaseModel
from .question import Question

class QuestionResponse(BaseModel):
    success: bool
    data: Optional[Question] = None
    error: Optional[str] = None