from domain.users.dto.create_user_dto import CreateUserDto
from domain.users.services.user_services import UserService
from infra.database.models.user import User
import logging
from fastapi.routing import APIRouter
from fastapi import status

users_routes = APIRouter(
    prefix="/users",
    tags=[
        "Users",
    ],
)


@users_routes.post("", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(new_user: CreateUserDto):
    try:
        user_service = UserService()
        return await user_service.create_user(new_user)
    except Exception as e:
        logging.error(f"Error caused due to : {e}")
        return {"error": "An error ocurred in the user creation"}
