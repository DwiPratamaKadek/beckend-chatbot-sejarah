from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    question: str
    answer: str
    img_url : Optional[str] = None