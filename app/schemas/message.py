from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from datetime import datetime
import uuid

from db.base import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    conversation_id = Column(String, ForeignKey("conversations.id"), nullable=False)

    role = Column(String, nullable=False)  # system | user | assistant | agent
    content = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)