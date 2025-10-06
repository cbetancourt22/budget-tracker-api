from sqlalchemy.orm import Session
from app.schemas import CategoryCreate, PurchaseCreate
from app.models import Category, Purchase
from datetime import date


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_category(self, category: CategoryCreate):
        db_category = Category(name=category.name)
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def get_categories(self):
        return self.db.query(Category).all()
