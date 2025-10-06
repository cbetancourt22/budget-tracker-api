from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db_connection import ServiceFactory
from app.schemas import PurchaseRead, PurchaseCreate
from app.service.purchase_service import PurchaseService
from datetime import date
from typing import List

router = APIRouter()

get_purchase_service = ServiceFactory(PurchaseService)


@router.post("/purchase/", response_model=PurchaseRead)
def create_purchase(
    purchase: PurchaseCreate, service: PurchaseService = Depends(get_purchase_service)
):
    return service.create_purchase(purchase)


@router.get("/purchases/{category_id}")
def get_purchases_by_category_id(
    category_id: int,
    start: date,
    end: date,
    service: PurchaseService = Depends(get_purchase_service),
):
    return service.get_purchases_by_category_id(category_id, start, end)
