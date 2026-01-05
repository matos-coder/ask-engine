from sqlalchemy.orm import Session
from app.schemas.client import Client


def get_client(db: Session, client_id: str) -> Client | None:
    return db.query(Client).filter(Client.id == client_id).first()


def create_client(db: Session, name: str) -> Client:
    client = Client(name=name)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client


def update_conversation_summary(
    db: Session,
    client: Client,
    summary: str
):
    client.conversation_summary = summary
    db.commit()
