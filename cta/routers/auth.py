from aiogram import Router
from aiogram.filters import Command

from ..dialogs.auth.states import AuthStateGroup


async def start_auth_dialog(message, dialog_manager):
    await dialog_manager.start(AuthStateGroup.set_username)

def auth_router():
    router = Router(name=__name__)
    router.message.register(start_auth_dialog, Command('start'))
    return router
