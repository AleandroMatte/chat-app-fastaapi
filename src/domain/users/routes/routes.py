from typing import Annotated, Optional

from fastapi.security import OAuth2PasswordRequestForm
from src.domain.users.dto.user_dtos import CreateUserDto, SharedUserDto
from domain.users.services.user_services import UserService
import logging
from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException, status

from src.domain.users.dto.token_dto import TokenDto

users_routes = APIRouter(
    prefix="/users",
    tags=[
        "Users",
    ],
)


@users_routes.post(
    "",
    response_model=Optional[SharedUserDto] | dict,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(new_user: CreateUserDto):
    try:
        user_service = UserService()
        return await user_service.create_user(new_user)
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Error caused due to : {e}")
        raise HTTPException(
            detail="An error ocurred in the user creation",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


@users_routes.post(
    path="/login",
    response_model=Optional[TokenDto] | dict,
    status_code=status.HTTP_201_CREATED,
)
async def login_user(user_login_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    try:
        user_service = UserService()
        return await user_service.login_user(
            username=user_login_data.username, password=user_login_data.password
        )
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(
            detail="Something went wrong logging in",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
