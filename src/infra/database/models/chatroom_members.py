import uuid
from pydantic import Field

from src.shared.BaseModel import CustomBaseModel


class ChatroomMembers(CustomBaseModel):
    _id: uuid.UUID = Field(default_factory=uuid.uuid4)
    chat_id: uuid.UUID
    user_id: uuid.UUID
