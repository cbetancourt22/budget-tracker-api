from fastapi import FastAPI
from app.controller import budget_controller
from app.database import Base, engine
from app.models import Category, Purchase  # your models

app = FastAPI(title="Budget Tracker API")

app.include_router(budget_controller.router)
