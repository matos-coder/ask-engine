from db.base import Base
from db.session import engine
from app.schemas.client import Client


def init_db():
    Base.metadata.create_all(bind=engine)
