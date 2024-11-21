from functools import lru_cache

from aiogram import Dispatcher, Bot, Router
from punq import Container, Scope

from core.infra.repositories.msg_repo.base import BaseMsgRepo
from core.infra.repositories.msg_repo.msg import MsgRepo
from core.logic.command.msg import GetMsgCommandHandler, AddMsgCommandHandler, GetMsgCommand, AddMsgCommand
from core.logic.mediator import Mediator
from core.settings.config import Settings


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(GetMsgCommandHandler)
    container.register(AddMsgCommandHandler)

    def init_settings() -> Settings:
        return Settings()

    def init_bot() -> Bot:
        settings: Settings = container.resolve(Settings)
        bot = Bot(token=settings.b_token)
        return bot

    def init_dispatcher() -> Dispatcher:
        return Dispatcher()

    def init_msg_repo() -> BaseMsgRepo:
        return MsgRepo()

    def init_mediator() -> Mediator:
        mediator = Mediator()

        mediator.register_command(GetMsgCommand, [container.resolve(GetMsgCommandHandler)])
        mediator.register_command(AddMsgCommand, [container.resolve(AddMsgCommandHandler)])

        return mediator

    container.register(Bot, factory=init_bot, scope=Scope.singleton)
    container.register(Dispatcher, factory=init_dispatcher, scope=Scope.singleton)
    container.register(Settings, factory=init_settings, scope=Scope.singleton)

    container.register(BaseMsgRepo, factory=init_msg_repo, scope=Scope.singleton)
    container.register(Mediator, factory=init_mediator, scope=Scope.singleton)

    return container
