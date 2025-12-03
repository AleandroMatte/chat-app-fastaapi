import logging
from typing import Annotated
from fastapi import APIRouter, HTTPException, Header

from src.domain.chatrooms.dtos.create_chatroom_dto import CreateChatroomDto
from src.domain.chatrooms.services.chatrooms_service import ChatroomService
from src.infra.database.models.chatroom import Chatrooms


chatroom_routes = APIRouter(prefix="/chats", tags=["Chatrooms"])


@chatroom_routes.post("", response_model=Chatrooms)
async def create_chatroom(
    username: Annotated[str | None, Header()], chatroom_data: CreateChatroomDto
):
    try:
        chatroom_service = ChatroomService()
        chatroom_service.create_chatroom(username, chatroom_data)
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"error occurred due to: {e}")
        return {"detail": "error ocurred when creating chat"}
