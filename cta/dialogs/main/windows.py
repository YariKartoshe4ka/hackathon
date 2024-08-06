from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const

from .states import MainStateGroup

main_menu = Window(
    Const("Banner Text"),
    Row(
        Button(Const('Моя коллекция'), id='my_deck'),
        Button(Const('Рейтинг'), id='rating'),
        Button(Const('Достижения'), id='achievements'),
    ),
    Row(
        Button(Const('Добавить карту'), id='add_card'),
        Button(Const('Поделиться'), id='share_card')
    ),
    state=MainStateGroup.main_menu,
)
