from sqlalchemy.orm import Session
from app.schemas import PurchaseCreate
from app.models import Purchase
from datetime import date


class PurchaseRepository:
    def __init__(self, db: Session):
        self.db = db

    # Purchases
    def create_purchase(self, purchase: PurchaseCreate):
        db_purchase = Purchase(**purchase.dict())
        self.db.add(db_purchase)
        self.db.commit()
        self.db.refresh(db_purchase)
        return db_purchase

    def get_purchases_by_category_id(self, category_id: int, start: date, end: date):
        return (
            self.db.query(Purchase)
            .filter(Purchase.category_id == category_id)
            .filter(Purchase.date >= start)
            .filter(Purchase.date <= end)
            .all()
        )
