from fastapi.routing import APIRouter

users_routes = APIRouter(
    prefix="/users",
    tags=[
        "Users",
    ],
)
