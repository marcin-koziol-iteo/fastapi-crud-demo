from fastapi import FastAPI, Depends
from sqlmodel import Session
from db import init_db, get_session
from models import Product
from crud import create_product

app = FastAPI()

init_db()

@app.post("/products/")
def add_product(product: Product, session: Session = Depends(get_session)):
    return create_product(session, product)


