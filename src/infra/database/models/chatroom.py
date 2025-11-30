from datetime import date
import uuid
from pydantic import BaseModel, Field


class Chatrooms(BaseModel):
    _id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    is_group: bool
    created_at: date
    metadata: dict
