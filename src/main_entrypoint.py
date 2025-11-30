from contextlib import asynccontextmanager
from logging import info
import os
from fastapi import FastAPI
from pymongo import AsyncMongoClient
from dotenv import load_dotenv

from domain.users.routes.routes import users_routes


@asynccontextmanager
async def db_lifespan(app: FastAPI):
    # Startup
    app.mongodb_client = AsyncMongoClient(os.environ["MONGO_CONNECTION_STR"])
    app.database = app.mongodb_client.get_database(os.environ["MONGO_DB_NAME"])
    ping_response = await app.database.command("ping")
    if int(ping_response["ok"]) != 1:
        raise Exception("Problem connecting to database cluster.")
    else:
        info("Connected to database cluster.")
    yield
    await app.mongodb_client.close()


load_dotenv()
app: FastAPI = FastAPI(lifespan=db_lifespan)
app.include_router(users_routes)
