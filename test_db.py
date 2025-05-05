from alembic import command
from alembic.config import Config
from db import get_session
from fastapi.testclient import TestClient
from main import app
from models import Product
from sqlmodel import Session
from sqlmodel import SQLModel
from sqlmodel import create_engine

DATABASE_URL = "postgresql+psycopg://crud:123qweasd@localhost:5432/crud_test"
engine = create_engine(DATABASE_URL)


def override_get_session():
    with Session(engine) as session:
        yield session


def create_test_db():
    SQLModel.metadata.create_all(engine)


def run_migrations():
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", DATABASE_URL)
    command.upgrade(alembic_cfg, "head")


run_migrations()

app.dependency_overrides[get_session] = override_get_session

client = TestClient(app)
