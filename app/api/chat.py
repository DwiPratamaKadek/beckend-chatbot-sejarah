from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.service.rag_engine import build_qa
from app.models.chat import ChatResponse, ChatRequest

router = APIRouter()
qa_chain = build_qa()

@router.post("/", response_model=ChatResponse)
async def text_chat(request: ChatRequest):
    try:
        result = qa_chain.invoke({"query" : request.query})
        return ChatResponse(
            question=request.query,
            answer=result["result"]
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
