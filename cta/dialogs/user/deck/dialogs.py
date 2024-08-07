from aiogram_dialog import Dialog

from ....dispatcher import dp
from . import windows


def deck_dialog():
    dialog = Dialog(
        windows.deck
    )
    dp.include_router(dialog)
