from infra.database.models.chatroom_members import ChatroomMembers
from shared.BaseRepository import BaseCollectionRepository


class ChatroomRepository(BaseCollectionRepository[ChatroomMembers]):
    model = ChatroomMembers

    def __init__(self):
        super().__init__("chatroom_membership")
