from pydantic import BaseModel

class ChatRequest(BaseModel):
    client_id: str
    question: str
