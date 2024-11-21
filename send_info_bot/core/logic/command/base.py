from abc import ABC, abstractmethod as abstract
from dataclasses import dataclass as datacls
from typing import TypeVar, Any, Generic


@datacls(frozen=True)
class BsCommand(ABC):
    ...


CT = TypeVar('CT', bound=BsCommand)
CR = TypeVar('CR', bound=Any)


@datacls(frozen=True)
class BsCommandHandler(ABC, Generic[CT, CR]):

    @abstract
    async def handle(self, command: CT) -> CR:
        ...
