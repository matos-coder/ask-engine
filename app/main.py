# app/main.py

from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.routes.ingest import router as ingest_router

app = FastAPI(title="Ask Engine")

app.include_router(chat_router, prefix="/chat")
app.include_router(ingest_router, prefix="/ingest")
