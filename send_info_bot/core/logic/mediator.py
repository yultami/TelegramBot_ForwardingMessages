from collections import defaultdict
from dataclasses import dataclass as datacls, field
from typing import Type, Iterable

from core.logic.command.base import CT, BsCommandHandler, CR, BsCommand
from core.logic.exceptions.mediator_exc import CommandHandlerNotRegistered


@datacls(eq=False)
class Mediator:
    command_map: dict[Type[CT], list[BsCommandHandler[CT, CR]]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )

    def register_command(self, command: Type[CT], command_handlers: Iterable[BsCommandHandler[CT, CR]]) -> None:

        self.command_map[command].extend(command_handlers)

    async def handle_command(self, command: BsCommand) -> Iterable[CR]:

        command_type = command.__class__
        print("command type:", command_type)
        handlers = self.command_map.get(command_type)
        print("handlers:", handlers)

        if not handlers:
            raise CommandHandlerNotRegistered(command_type)

        return [await handler.handle(command) for handler in handlers]