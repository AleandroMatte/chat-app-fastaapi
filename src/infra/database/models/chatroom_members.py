from bson import ObjectId
from pydantic import BaseModel, Field


class ChatroomMembers(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    chat_id: str
    user_id: str
