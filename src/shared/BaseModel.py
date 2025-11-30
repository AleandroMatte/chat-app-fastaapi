import uuid
from pydantic import BaseModel, Field, field_serializer


class CustomBaseModel(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, alias="_id")

    @field_serializer("id", when_used="always", mode="plain")
    def serialize_id(self, value: uuid.UUID):
        return str(value)
