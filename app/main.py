from fastapi import FastAPI
from app.controller import purchase_controller, category_controller
from app.database import Base, engine
from app.models import Category, Purchase  # your models

app = FastAPI(title="Budget Tracker API")

app.include_router(purchase_controller.router)
app.include_router(category_controller.router)
