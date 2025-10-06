from pydantic import BaseModel
from datetime import date
from typing import Optional


class PurchaseCreate(BaseModel):
    amount: float
    description: Optional[str] = None
    date: date
    category_id: int


class PurchaseRead(PurchaseCreate):
    id: int


class CategoryCreate(BaseModel):
    name: str


class CategoryRead(CategoryCreate):
    id: int
