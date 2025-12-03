from pydantic import BaseModel


class TokenDto(BaseModel):
    token: str


class UserTokenData(BaseModel):
    id: str
    username: str
