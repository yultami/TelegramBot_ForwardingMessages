from core.domain.entities.channel import Channel
from core.domain.entities.msg import Msg
from core.infra.repositories.msg_repo.base import BaseMsgRepo


class MsgRepo(BaseMsgRepo):
    def __init__(self):
        self.data: dict[int, dict[int, list[Msg]]] = {}

    def get_msg(self):
        return self.data

    def add_msg(self, channel: Channel, msg: Msg):
        user_id = msg.msg_aiogram.from_user.id
        if user_id not in self.data:
            self.data[user_id] = {}
        if channel.id not in self.data[user_id]:
            self.data[user_id][channel.id] = []
        self.data[user_id][channel.id].append(msg)
