from pydantic import BaseModel
from typing import List
from .domain import Domain

class Option(BaseModel):
    text: str
    is_correct: bool

class Question(BaseModel):
    question_text: str
    options: List[Option]
    explanation: str
    domain: Domain