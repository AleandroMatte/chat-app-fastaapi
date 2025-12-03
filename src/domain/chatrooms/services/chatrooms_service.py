from fastapi import HTTPException, status
from src.domain.chatrooms.dtos.create_chatroom_dto import CreateChatroomDto
from src.domain.chatrooms.repositories.chatroom_repository import ChatroomRepository
from src.domain.users.repositories.user_repository import UserRepository
from src.infra.database.models.chatroom import Chatrooms
from src.infra.database.models.chatroom_members import ChatroomMembers


class ChatroomService:
    def __init__(self):
        self.chatroom_repository = ChatroomRepository()
        self.user_repository = UserRepository()
        self.chatroom_membership_repository = ChatroomRepository()

    async def create_chatroom(self, username: str, chatroom_data: CreateChatroomDto):
        new_chatroom = Chatrooms.model_validate(chatroom_data, from_attributes=True)
        await self.chatroom_repository.insert_one(new_chatroom)
        user = await self.user_repository.find_user_by_name(username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User not found"
            )
        await self.chatroom_membership_repository.insert_one(
            ChatroomMembers(chat_id=new_chatroom.id, user_id=user.id)
        )
