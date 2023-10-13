from aiogram import Bot, Dispatcher
from core.handlers.basic import get_start
import asyncio

TOKEN = "5739946001:AAFKeydE05CFWRN2YjYXIuGeGU-ZWSaMeJU"
ADMIN_ID = "1576384897"


async def start_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text="Бот - онлайн.")


async def stop_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text="Бот - офлайн")


async def start():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
