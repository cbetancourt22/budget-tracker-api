from sqlalchemy.orm import Session
from app.schemas import CategoryCreate, PurchaseCreate
from app.models import Category, Purchase
from datetime import date


class BudgetRepository:
    def __init__(self, db: Session):
        self.db = db

    # Categories
    def create_category(self, name: str):
        db_category = Category(name=name)
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def get_categories(self):
        return self.db.query(Category).all()

    # Purchases
    def create_purchase(self, purchase: PurchaseCreate):
        db_purchase = Purchase(**purchase.dict())
        self.db.add(db_purchase)
        self.db.commit()
        self.db.refresh(db_purchase)
        return db_purchase

    def get_purchases_by_category_and_date(
        self, category_id: int, start: date, end: date
    ):
        return (
            self.db.query(Purchase)
            .filter(Purchase.category_id == category_id)
            .filter(Purchase.date >= start)
            .filter(Purchase.date <= end)
            .all()
        )
