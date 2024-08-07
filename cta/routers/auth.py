from aiogram import Router
from aiogram.filters import Command

from ..database.client import find_user_by_tg_id
from ..dialogs.auth.states import AuthStateGroup
from ..dialogs.user.menu.states import UserMenuStateGroup


async def start_auth_dialog(message, dialog_manager):
    if find_user_by_tg_id(message.from_user.id) is None:
        await dialog_manager.start(AuthStateGroup.set_username)
    else:
        await dialog_manager.start(UserMenuStateGroup.menu)


def auth_router():
    router = Router(name=__name__)
    router.message.register(start_auth_dialog, Command('start'))
    return router
