from pydantic import BaseModel


class CreateUserDto(BaseModel):
    username: str
    password: str


class SharedUserDto(BaseModel):
    id: str
    username: str
