from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import SessionLocal
from app.service.budget_service import BudgetService
from datetime import date
from typing import List

router = APIRouter(prefix="/budget")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/categories/", response_model=schemas.CategoryRead)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    service = BudgetService(db)
    return service.repo.create_category(category)


@router.get("/categories/", response_model=List[schemas.CategoryRead])
def list_categories(db: Session = Depends(get_db)):
    service = BudgetService(db)
    return service.repo.get_categories()


@router.post("/purchases/", response_model=schemas.PurchaseRead)
def create_purchase(purchase: schemas.PurchaseCreate, db: Session = Depends(get_db)):
    service = BudgetService(db)
    return service.repo.create_purchase(purchase)


@router.get("/spending/{category_id}")
def get_spending(
    category_id: int, start: date, end: date, db: Session = Depends(get_db)
):
    service = BudgetService(db)
    return service.get_category_spending(category_id, start, end)
