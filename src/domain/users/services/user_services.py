from fastapi import HTTPException, status
from domain.users.dto.create_user_dto import CreateUserDto
from domain.users.repositories.user_repository import UserRepository
from infra.database.models.user import User


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def create_user(self, user_data: CreateUserDto):
        if await self.user_repository.find_user_by_name(user_data.username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Username Already exists"
            )
        new_user = User.model_validate(user_data, from_attributes=True)
        await self.user_repository.insert_one(new_user)
        return await self.user_repository.get_by_id(new_user.id)
