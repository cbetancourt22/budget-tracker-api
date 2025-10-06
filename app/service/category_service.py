from app.repository.category_repository import CategoryRepository
from sqlalchemy.orm import Session
from datetime import date

from app.schemas import CategoryCreate


class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def create_category(self, category: CategoryCreate):
        return self.repository.create_category(category)

    def get_categories(self):
        return self.repository.get_categories()
