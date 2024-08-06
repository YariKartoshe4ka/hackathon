from aiogram_dialog import Dialog

from ...dispatcher import dp
from . import windows


def main_dialog():
    dialog = Dialog(
        windows.main_menu
    )
    dp.include_router(dialog)
