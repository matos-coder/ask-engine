from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.schemas.conversation import Conversation

EXPIRATION_HOURS = 24

def get_or_create_conversation(db: Session, client_id: str) -> Conversation:
    convo = (
        db.query(Conversation)
        .filter(
            Conversation.client_id == client_id,
            Conversation.is_active == True
        )
        .first()
    )

    if convo:
        if datetime.utcnow() - convo.last_activity_at > timedelta(hours=EXPIRATION_HOURS):
            convo.is_active = False
            convo.closed_at = datetime.utcnow()
            db.commit()
        else:
            convo.last_activity_at = datetime.utcnow()
            db.commit()
            return convo

    new_convo = Conversation(client_id=client_id)
    db.add(new_convo)
    db.commit()
    db.refresh(new_convo)
    return new_convo
