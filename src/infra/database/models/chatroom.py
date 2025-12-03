from datetime import date, datetime
from bson import ObjectId
from pydantic import BaseModel, Field


class Chatrooms(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    name: str
    created_at: date = Field(default_factory=lambda: datetime.now().date)
    metadata: dict
