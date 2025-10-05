from fastapi import FastAPI
from app.controller import user_controller

app = FastAPI()

app.include_router(user_controller.router, prefix="/users", tags=["Users"])
