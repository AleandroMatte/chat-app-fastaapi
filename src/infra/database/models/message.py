from datetime import datetime
from typing import Literal
import uuid
from pydantic import BaseModel, Field


class Message(BaseModel):
    _id: uuid.UUID = Field(default_factory=uuid.uuid4)
    chat_id: uuid.UUID
    sender_id: uuid.UUID
    content: str
    content_type: Literal["text", "image"]
    sent_at: datetime
