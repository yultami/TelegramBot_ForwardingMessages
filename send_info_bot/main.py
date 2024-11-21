import asyncio

from aiogram import Bot, Dispatcher
from punq import Container

from core.app.hndl.msg_h import catch_msg_router
from core.app.hndl.start_h import start_router
from core.app.mthd.sender_method import start_schedule_send
from core.logic.container import init_container


async def main():
    container: Container = init_container()
    bot: Bot = container.resolve(Bot)
    dp: Dispatcher = container.resolve(Dispatcher)
    dp.include_routers(start_router, catch_msg_router)

    await asyncio.gather(start_schedule_send(bot), dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()))


if __name__ == '__main__':
    asyncio.run(main())
