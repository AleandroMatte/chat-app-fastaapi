import os
import uuid
from pymongo import AsyncMongoClient
from pymongo.collection import Collection
from pymongo.asynchronous.database import AsyncDatabase
import pytest

from src.infra.database.models.user import User


@pytest.mark.integration
@pytest.mark.asyncio
async def test_has_necessary_database():
    connection = AsyncMongoClient(os.environ["MONGO_CONNECTION_STR"], timeoutMS=5000)
    database = connection.get_database(os.environ["MONGO_DB_NAME"])
    response = await database.command("ping", check=False)
    assert response["ok"] == 1, "Could not connect to database!"


@pytest.mark.mock_data
@pytest.mark.integration
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user",
    (
        User(_id=uuid.uuid4(), username="Aleandro matteoni"),
        User(_id=uuid.uuid4(), username="Yuri Marim"),
        User(_id=uuid.uuid4(), username="Potato Bro"),
    ),
)
async def test_database_accepts_writes(database_connection: AsyncDatabase, user: User):
    users_collection: Collection = database_connection.get_collection("users")
    await users_collection.insert_one(user.model_dump(by_alias=True))
