import uuid
from pydantic import BaseModel, Field


class User(BaseModel):
    _id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: str
