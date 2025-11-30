import uuid
from pydantic import BaseModel, Field


class ChatroomMembers(BaseModel):
    _id: uuid.UUID = Field(default_factory=uuid.uuid4)
    chat_id: uuid.UUID
    user_id: uuid.UUID
