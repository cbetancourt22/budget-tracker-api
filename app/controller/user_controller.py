from fastapi import APIRouter, Depends
from app.service.user_service import UserService

router = APIRouter()

@router.get("/")
def get_users(service: UserService = Depends()):
    return service.get_all_users()
