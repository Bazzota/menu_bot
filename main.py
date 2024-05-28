import asyncio
from aiogram import Bot, Dispatcher

from config import main_config


async def main():
    BOT = Bot(main_config.tg_bot.token)
    dp = Dispatcher()

    await dp.start_polling(BOT)


if __name__ == '__main__':
    asyncio.run(main())