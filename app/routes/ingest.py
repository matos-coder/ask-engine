from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
import os, uuid, shutil

from app.ingestion.pipeline import ingest_documents
from app.ingestion.loaders.pdf_loader import load_pdf
from app.ingestion.loaders.word_loader import load_word
from app.ingestion.loaders.url_loader import load_url
from app.ingestion.loaders.text_loader import load_text
from app.schemas.ingest import IngestRequest

router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
def ingest(
    data: IngestRequest,
    files: List[UploadFile] = File(default=[])
):
    if not data.client_id:
        raise HTTPException(status_code=400, detail="client_id required")

    documents = []

    # FILES
    for file in files:
        ext = file.filename.split(".")[-1].lower()
        temp_path = f"{UPLOAD_DIR}/{uuid.uuid4()}.{ext}"

        with open(temp_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        if ext == "pdf":
            documents.extend(load_pdf(temp_path))
        elif ext in ["docx", "doc"]:
            documents.extend(load_word(temp_path))
        else:
            raise HTTPException(400, f"Unsupported file: {file.filename}")

        os.remove(temp_path)

    # URLS
    if data.urls:
        for url in data.urls:
            documents.extend(load_url(url))

    # TEXTS
    if data.texts:
        for text in data.texts:
            documents.extend(load_text(text))

    if not documents:
        raise HTTPException(400, "No content provided")

    chunks = ingest_documents(documents, data.client_id)

    return {
        "status": "success",
        "chunks_added": chunks
    }
