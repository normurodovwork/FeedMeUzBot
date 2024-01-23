import asyncio
import os

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from handlers import handlers_router

import logging
import sys

load_dotenv()

TOKEN = os.getenv('TOKEN')
dp = Dispatcher()


async def main() -> None:
    dp.include_router(handlers_router)
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
