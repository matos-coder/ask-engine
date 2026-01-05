from pydantic import BaseModel

class UrlIngestRequest(BaseModel):
    client_id: str
    url: str
