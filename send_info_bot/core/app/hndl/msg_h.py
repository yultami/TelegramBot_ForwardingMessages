from collections import defaultdict

from aiogram import Router
from aiogram.types import Message
from punq import Container

from core.logic.command.msg import AddMsgCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator
from core.settings.config import Settings

catch_msg_router = Router()


@catch_msg_router.message()
async def msg_h(msg: Message):
    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    settings: Settings = container.resolve(Settings)
    if msg.media_group_id:
        media_gs = defaultdict(list)
        media_gs[msg.media_group_id].append(msg)
        del media_gs[msg.media_group_id]
    await mediator.handle_command(AddMsgCommand(settings.channel_id, msg))