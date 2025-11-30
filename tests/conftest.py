import logging
import os
from dotenv import load_dotenv
from pymongo import AsyncMongoClient
import pytest
import pytest_asyncio


@pytest.fixture(scope="session", autouse=True)
def load_environ_vars():
    is_loaded = load_dotenv()
    if not is_loaded:
        logging.info("Unable to load .env file, using server bound variables")
    else:
        logging.info("All variables loaded from dotenv file")


@pytest_asyncio.fixture
async def database_connection():
    connection = AsyncMongoClient(os.environ["MONGO_CONNECTION_STR"], timeoutMS=5000)
    db = connection.get_database(os.environ["MONGO_DB_NAME"])
    yield db
    await db.client.close()
    await connection.aclose()
