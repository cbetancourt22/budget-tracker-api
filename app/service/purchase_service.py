from typing import List
from decimal import Decimal, getcontext
from app.models import Purchase
from app.repository.purchase_repository import PurchaseRepository
from app.schemas import PurchaseCreate
from sqlalchemy.orm import Session
from datetime import date

getcontext().prec = 28


class PurchaseService:
    def __init__(self, db: Session):
        self.repository = PurchaseRepository(db)

    def create_purchase(self, purchase: PurchaseCreate):
        return self.repository.create_purchase(purchase)

    def get_purchases_by_category_id(self, category_id: int, start: date, end: date):
        purchases = self.repository.get_purchases_by_category_id(
            category_id, start, end
        )
        total = self.get_total_spent(purchases)
        return {"category_id": category_id, "total": total, "purchases": purchases}

    def get_total_spent(self, purchases: List[Purchase]) -> float:
        total = Decimal("0")
        for purchase in purchases:
            total += Decimal(str(purchase.amount))

        return float(round(total, 2))
