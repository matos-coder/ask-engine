from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest
from app.rag.chat import answer_question

router = APIRouter()

@router.post("")
def chat(req: ChatRequest):
    if not req.client_id:
        raise HTTPException(status_code=400, detail="client_id is required")

    return answer_question(
        question=req.question,
        client_id=req.client_id
    )
