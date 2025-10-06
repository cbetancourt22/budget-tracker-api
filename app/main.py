from fastapi import FastAPI
from app.controller import budget_controller
from app.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Budget Tracker API")

app.include_router(budget_controller.router)
