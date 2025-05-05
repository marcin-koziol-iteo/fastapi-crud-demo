from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    description: Optional[str] = None
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
