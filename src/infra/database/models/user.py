from pydantic import BaseModel, Field, SecretStr
from bson import ObjectId


class User(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    username: str
    password: SecretStr | bytes
