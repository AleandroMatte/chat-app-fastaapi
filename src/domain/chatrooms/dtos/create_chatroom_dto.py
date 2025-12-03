from pydantic import BaseModel


class CreateChatroomDto(BaseModel):
    name: str
    metadata: dict
    additional_participants = list[str] = []
