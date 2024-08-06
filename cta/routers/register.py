from aiogram_dialog import setup_dialogs

from ..dispatcher import dp
from .auth import auth_router


def register_routers():
    dp.include_router(auth_router())
    setup_dialogs(dp)
