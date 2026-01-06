from sqlalchemy import Column, String, Text, Boolean, DateTime
from datetime import datetime
import uuid

from db.base import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)

    enable_agent_handoff = Column(Boolean, default=False)
    #handoff_message = Column(String, default="Would you like to talk to our agent?")

    memory_enabled = Column(Boolean, default=True)
    system_prompt = Column(Text, default="You are a helpful assistant.")
    conversation_summary = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
