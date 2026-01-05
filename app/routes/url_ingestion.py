from fastapi import APIRouter

from app.ingestion.loaders.url_loader import load_url
from app.ingestion.pipeline import ingest_documents
from app.schemas.url_ingestion import UrlIngestRequest


router = APIRouter()

@router.post("")
def ingest_url(req: UrlIngestRequest):
    documents = load_url(req.url)
    chunks = ingest_documents(documents, req.client_id)

    return {
        "status": "success",
        "chunks_added": chunks
    }
