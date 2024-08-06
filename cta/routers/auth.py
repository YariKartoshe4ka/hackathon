from aiogram import Router
from aiogram.filters import Command

from ..database.client import find_user_by_tg_id
from ..dialogs.auth.states import AuthStateGroup
from ..dialogs.main.states import MainStateGroup


async def start_auth_dialog(message, dialog_manager):
    user = find_user_by_tg_id(message.from_user.id)
    if user is None:
        print(message.from_user.id)
        print(user)
        await dialog_manager.start(AuthStateGroup.set_username)
    else:
        await dialog_manager.start(MainStateGroup.main_menu)


def auth_router():
    router = Router(name=__name__)
    router.message.register(start_auth_dialog, Command('start'))
    return router
