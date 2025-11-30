from infra.database.models.user import User
from shared.BaseRepository import BaseCollectionRepository


class UserRepository(BaseCollectionRepository[User]):
    model = User

    def __init__(self):
        super().__init__("users")
