from datetime import datetime
from typing import Literal
from bson import ObjectId
from pydantic import BaseModel, Field


class Message(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    chat_id: str
    sender_id: str
    content: str
    content_type: Literal["text", "image"]
    sent_at: datetime
