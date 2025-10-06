from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db_connection import ServiceFactory
from app.schemas import CategoryCreate, CategoryRead
from app.service.category_service import CategoryService
from datetime import date
from typing import List

router = APIRouter()

get_category_service = ServiceFactory(CategoryService)


@router.post("/category/", response_model=CategoryRead)
def create_category(
    category: CategoryCreate, service: CategoryService = Depends(get_category_service)
):
    return service.create_category(category)


@router.get("/category/", response_model=List[CategoryRead])
def get_categories(service: CategoryService = Depends(get_category_service)):
    return service.get_categories()
