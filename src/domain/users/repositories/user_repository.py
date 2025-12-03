from infra.database.models.user import User
from shared.BaseRepository import BaseCollectionRepository


class UserRepository(BaseCollectionRepository[User]):
    model = User

    def __init__(self):
        super().__init__("users")

    async def find_user_by_name(self, username: str):
        return await self.collection.find_one({"username": username})
