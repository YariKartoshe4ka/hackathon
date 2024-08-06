from os import getenv

from aiogram import Bot
from dotenv import load_dotenv

from .dialogs.register import register_dialogs
from .dispatcher import dp
from .routers.register import register_routers


def main():
    load_dotenv()
    bot = Bot(getenv('BOT_TOKEN'))

    register_dialogs()
    register_routers()
    dp.run_polling(bot)
