import sys


sys.path.append("src/")
import os
from pymongo import AsyncMongoClient
import pytest


@pytest.mark.integration
@pytest.mark.asyncio
async def test_has_necessary_database():
    connection = AsyncMongoClient(os.environ["MONGO_CONNECTION_STR"], timeoutMS=5000)
    database = connection.get_database(os.environ["MONGO_DB_NAME"])
    response = await database.command("ping", check=False)
    assert response["ok"] == 1, "Could not connect to database!"
