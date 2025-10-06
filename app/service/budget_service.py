from app.repository.budget_repository import BudgetRepository
from sqlalchemy.orm import Session
from datetime import date


class BudgetService:
    def __init__(self, db: Session):
        self.repo = BudgetRepository(db)

    def add_category(self, name: str):
        return self.repo.create_category(name)

    def add_purchase(self, purchase):
        return self.repo.create_purchase(purchase)

    def get_category_spending(self, category_id: int, start: date, end: date):
        purchases = self.repo.get_purchases_by_category_and_date(
            category_id, start, end
        )
        total = sum(p.amount for p in purchases)
        return {"category_id": category_id, "total": total, "purchases": purchases}
