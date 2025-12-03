from infra.database.models.chatroom import Chatrooms
from shared.BaseRepository import BaseCollectionRepository


class ChatroomRepository(BaseCollectionRepository[Chatrooms]):
    model = Chatrooms

    def __init__(self):
        super().__init__("chatrooms")
