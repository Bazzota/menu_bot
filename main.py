import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import main_config
from heandlers.heandlers import router

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='[{asctime}] #{levelname:8} {filename}:'
               '{lineno} - {name} - {message}',
        style='{'
    )

    logger.info('Starting bot')

    BOT = Bot(main_config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(BOT)


if __name__ == '__main__':
    asyncio.run(main())