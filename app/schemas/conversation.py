from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Index
from datetime import datetime
import uuid

from db.base import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    client_id = Column(String, ForeignKey("clients.id"), nullable=False)

    is_active = Column(Boolean, default=True)
    last_activity_at = Column(DateTime, default=datetime.utcnow)

    created_at = Column(DateTime, default=datetime.utcnow)
    closed_at = Column(DateTime, nullable=True)

    __table_args__ = (
        Index("idx_active_conversation", "client_id", "is_active"),
    )
