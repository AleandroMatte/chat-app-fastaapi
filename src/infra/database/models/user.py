import uuid
from pydantic import Field

from shared.BaseModel import CustomBaseModel


class User(CustomBaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, alias="_id")
    username: str
