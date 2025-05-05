from sqlmodel import Session
from sqlmodel import SQLModel
from sqlmodel import create_engine

DATABASE_URL = "postgresql+psycopg://crud:123qweasd@localhost:5432/crud"
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
