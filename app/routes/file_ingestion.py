import os
import shutil
import uuid
from fastapi import APIRouter, HTTPException, UploadFile, File
from typing import List

from app.ingestion.loaders.pdf_loader import load_pdf
from app.ingestion.loaders.word_loader import load_word
from app.ingestion.pipeline import ingest_documents

router = APIRouter()

@router.post("")
def ingest_file(
    client_id: str,
    files: List[UploadFile] = File(...)
):
    documents = []

    for file in files:
        ext = file.filename.split(".")[-1].lower()
        temp_path = f"uploads/{uuid.uuid4()}.{ext}"

        with open(temp_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        if ext == "pdf":
            documents.extend(load_pdf(temp_path))
        elif ext in ["docx", "doc"]:
            documents.extend(load_word(temp_path))
        else:
            raise HTTPException(400, "Unsupported file")

        os.remove(temp_path)

    chunks = ingest_documents(documents, client_id)

    return {
        "status": "success",
        "chunks_added": chunks
    }
