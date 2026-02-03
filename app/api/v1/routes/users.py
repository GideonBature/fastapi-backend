from fastapi import APIRouter, HTTPException
from app.services.user_service import UserService
from app.exceptions.user import UserNotFoundError
from app.schemas.user import UserResponse

router = APIRouter()
user_service = UserService()

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    try:
        return user_service.get_user(user_id)
    except UserNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))