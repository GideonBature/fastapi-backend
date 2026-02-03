from fastapi import APIRouter
from app.api.v1.routes import users

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["users"]
)