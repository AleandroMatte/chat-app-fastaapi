from datetime import date
import uuid
from pydantic import Field

from src.shared.BaseModel import CustomBaseModel


class Chatrooms(CustomBaseModel):
    _id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    is_group: bool
    created_at: date
    metadata: dict
