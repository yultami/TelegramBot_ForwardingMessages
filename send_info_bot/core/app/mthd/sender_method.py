import asyncio

from aiogram import Bot
from aiogram.utils.media_group import MediaGroupBuilder
from punq import Container

from core.logic.command.msg import GetMsgCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator


class MsgSenderService:
    def __init__(self, bot):
        self.bot = bot

    async def _get_text(self, msg):
        first_name = msg.msg_aiogram.from_user.first_name
        username = msg.msg_aiogram.from_user.username
        if msg.msg_aiogram.text:
            text = f"<b>Отправил/а:</b> {first_name}, <b>username:</b> @{username} \n" + msg.msg_aiogram.text
            return text
        if msg.msg_aiogram.caption:
            caption = f"<b>Отправил/а:</b> {first_name}, <b>username:</b> @{username} \n" \
                               + msg.msg_aiogram.caption
            return caption

    async def _send_answer(self, user_id):
        await self.bot.send_message(chat_id=user_id, text="Ваш текст отправлен! Приятного дня!")

    async def _resend_answer(self, group_id, text):
        await self.bot.send_message(chat_id=group_id, text=text, parse_mode='HTML')

    async def _resend_media_answer(self, group_id, media_g):
        await self.bot.send_media_group(chat_id=group_id, media=media_g.build())

    async def send_media(self):
        container: Container = init_container()
        mediator: Mediator = container.resolve(Mediator)
        media, *_ = await mediator.handle_command(GetMsgCommand())
        while media:
            user_id, group_id_and_msg = media.popitem()
            media_g = MediaGroupBuilder()
            await self._send_answer(user_id)
            for group_id, msg in group_id_and_msg.items():
                for item in msg:
                    if item.msg_aiogram.text is not None:
                        text = await self._get_text(item)
                        await self._resend_answer(group_id, text)
                        return
                    if item.msg_aiogram.caption is not None:
                        media_g.caption = await self._get_text(item)
                    if item.msg_aiogram.photo is not None:
                        media_g.add_photo(item.msg_aiogram.photo[-1].file_id, parse_mode='HTML')
                if media_g:
                    await self._resend_media_answer(group_id, media_g)
            return


async def start_schedule_send(bot: Bot):
    msg_sender_service = MsgSenderService(bot)
    while True:
        await asyncio.sleep(15)
        await msg_sender_service.send_media()