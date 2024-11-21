from dataclasses import dataclass as datacls

from aiogram.types import Message

from core.domain.entities.channel import Channel
from core.domain.entities.msg import Msg
from core.infra.repositories.msg_repo.base import BaseMsgRepo
from core.logic.command.base import BsCommand, BsCommandHandler


@datacls(frozen=True)
class GetMsgCommand(BsCommand):
    ...


@datacls(frozen=True)
class AddMsgCommand(BsCommand):
    channel_id: int
    msg: Message


@datacls(frozen=True)
class GetMsgCommandHandler(BsCommandHandler[GetMsgCommand, dict[int, dict[int, list[Msg]]]]):
    message_repository: BaseMsgRepo

    async def handle(self, command: GetMsgCommand) -> dict[int, dict[int, list[Msg]]]:
        return self.message_repository.get_msg()


@datacls(frozen=True)
class AddMsgCommandHandler(BsCommandHandler[AddMsgCommand, None]):
    message_repository: BaseMsgRepo

    async def handle(self, command: AddMsgCommand) -> None:
        channel = Channel(
            id=command.channel_id
        )
        msg = Msg(
            msg_aiogram=command.msg
        )

        return self.message_repository.add_msg(channel, msg)


