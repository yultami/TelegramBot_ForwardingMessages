from abc import ABC, abstractmethod as abstract

from core.domain.entities.channel import Channel
from core.domain.entities.msg import Msg


class BaseMsgRepo(ABC):

    @abstract
    def get_msg(self) -> dict[int, dict[int, list[Msg]]]:
        ...

    @abstract
    def add_msg(self, channel: Channel, msg: Msg) -> None:
        ...