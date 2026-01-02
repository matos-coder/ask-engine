# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from app.rag.chat import answer_question

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(req: ChatRequest):
    return {"answer": answer_question(req.question)}
