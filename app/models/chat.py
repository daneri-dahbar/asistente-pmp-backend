from pydantic import BaseModel, Field
from typing import Optional, Dict, List

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    message_history: List[ChatMessage] = Field(default_factory=list)
    max_tokens: Optional[int] = 4096
    temperature: Optional[float] = 0.7

class ChatResponse(BaseModel):
    response: str
    usage: Dict[str, int] = Field(default_factory=dict)