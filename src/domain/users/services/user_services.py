from fastapi import HTTPException, status
from src.domain.users.dto.user_dtos import CreateUserDto
from domain.users.repositories.user_repository import UserRepository
from infra.database.models.user import User
from bcrypt import gensalt, hashpw, checkpw

from src.domain.users.dto.token_dto import TokenDto
from src.providers.token_provider import TokenProvider


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.token_provider = TokenProvider()

    async def create_user(self, user_data: CreateUserDto):
        if await self.user_repository.find_user_by_name(user_data.username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Username Already exists"
            )
        user_data.password = hashpw(user_data.password.encode(), gensalt())
        new_user = User.model_validate(user_data, from_attributes=True)
        await self.user_repository.insert_one(new_user)
        return await self.user_repository.get_by_id(new_user.id)

    async def login_user(self, username: str, password: str) -> TokenDto:
        user = await self.user_repository.find_user_by_name(username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Username does not exist"
            )
        if not checkpw(password.encode(), user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials"
            )
        token = await self.token_provider.create_token(data={"username": user.username})
        return {"token": token}
