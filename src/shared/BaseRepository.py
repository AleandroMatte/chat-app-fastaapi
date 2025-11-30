import os
from typing import Generic, Literal, Optional, Type, TypeVar
from pydantic import BaseModel
from pymongo.collection import Collection
from src.main_entrypoint import app

type AllowedCollections = Literal[
    "users", "messages", "chatrooms", "chatroom_membership"
]
T = TypeVar("T", bound=BaseModel)


class BaseCollectionRepository(Generic[T]):
    model: Type[T]

    def __init__(self, collection_name: AllowedCollections):
        self.collection: Collection = app.mongodb_client[os.environ["MONGO_DB_NAME"]][
            collection_name
        ]

    async def get_by_id(self, object_id: str) -> Optional[T]:
        document = await self.collection.find_one({"_id": object_id})
        if not document:
            return None
        return self.model.model_validate(document)

    async def insert_one(self, data: T) -> T:
        created_item = await self.collection.insert_one(data.model_dump())
        return self.model.model_validate(created_item, from_attributes=True)
