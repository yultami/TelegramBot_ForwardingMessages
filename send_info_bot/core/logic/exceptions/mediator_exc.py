from dataclasses import dataclass as datacls

from core.logic.exceptions.base import LogicException


@datacls
class CommandHandlerNotRegistered(LogicException):
    command_type: type

    @property
    def msg(self) -> str:
        return f'Command handlers for "{self.command_type}" are not registered'