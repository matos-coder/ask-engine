from pydantic import BaseModel

class TextIngestRequest(BaseModel):
    client_id: str
    text: str
