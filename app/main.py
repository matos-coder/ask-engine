# app/main.py

from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.routes.text_ingest import router as text_ingest_router
from app.routes.file_ingestion import router as file_ingest_router
from app.routes.url_ingestion import router as url_ingest_router
from dotenv import load_dotenv
load_dotenv()


app = FastAPI(title="Ask Engine")

app.include_router(chat_router, prefix="/chat")
app.include_router(text_ingest_router, prefix="/text")
app.include_router(file_ingest_router, prefix="/file")
app.include_router(url_ingest_router, prefix="/url")
# app.include_router(ingest_router, prefix="/ingest")
