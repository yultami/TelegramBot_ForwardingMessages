from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

start_router = Router()


@start_router.message(CommandStart())
async def start_command(msg: Message):
    await msg.answer("Привет, я был создан для пересылки сообщений!")

