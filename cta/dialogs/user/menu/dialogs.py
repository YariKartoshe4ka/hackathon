from aiogram_dialog import Dialog

from ....dispatcher import dp
from . import windows


def menu_dialog():
    dialog = Dialog(
        windows.menu
    )
    dp.include_router(dialog)
