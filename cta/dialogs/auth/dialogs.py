from aiogram_dialog import Dialog

from ...dispatcher import dp
from . import windows


def auth_dialog():
    dialog = Dialog(
        windows.set_username,
        windows.set_skills,
        windows.set_skill
    )
    dp.include_router(dialog)
