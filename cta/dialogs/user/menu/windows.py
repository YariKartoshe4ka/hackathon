from aiogram.types import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Row, Start
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const

from ..deck.states import UserDeckStateGroup
from .states import UserMenuStateGroup

menu = Window(
    StaticMedia(path='images/1.webp', type=ContentType.PHOTO),
    Row(
        Start(Const('Моя коллекция'), id='my_deck', state=UserDeckStateGroup.deck),
        Button(Const('Рейтинг'), id='rating'),
        Button(Const('Достижения'), id='achievements'),
    ),
    Row(
        Button(Const('Добавить карту'), id='add_card'),
        Button(Const('Поделиться'), id='share_card')
    ),
    state=UserMenuStateGroup.menu,
)
