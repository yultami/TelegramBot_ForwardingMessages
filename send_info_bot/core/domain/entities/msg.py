from dataclasses import dataclass

from aiogram.types import Message as MessageAiogram


@dataclass
class Msg:
    msg_aiogram: MessageAiogram