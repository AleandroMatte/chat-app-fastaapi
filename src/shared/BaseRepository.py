import os
from typing import Generic, Literal, Optional, Type, TypeVar
from pydantic import BaseModel
from pymongo import AsyncMongoClient
from pymongo.collection import Collection

type AllowedCollections = Literal[
    "users", "messages", "chatrooms", "chatroom_membership"
]
T = TypeVar("T", bound=BaseModel)


class BaseCollectionRepository(Generic[T]):
    model: Type[T]

    def __init__(self, collection_name: AllowedCollections):
        self.collection: Collection = (
            AsyncMongoClient(os.environ["MONGO_CONNECTION_STR"])
            .get_database(os.environ["MONGO_DB_NAME"])
            .get_collection(collection_name)
        )

    async def get_by_id(self, object_id: str) -> Optional[T]:
        document = await self.collection.find_one({"_id": object_id})
        if not document:
            return None
        return self.model.model_validate(document)

    async def insert_one(self, data: T):
        await self.collection.insert_one(data.model_dump())
