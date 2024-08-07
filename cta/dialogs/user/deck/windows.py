from aiogram.types import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Cancel, Row
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const

from .states import UserDeckStateGroup

images = ['images/image1.webp', 'images/image2.webp', 'images/image3.webp']


# async def change_text(c, button, manager):
#     user_data = manager.current_context().dialog_data
#     user_data['text_index'] = (user_data['text_index'] + 1) % len(categories)
#     await manager.update({"text": categories[user_data['text_index']]})


# async def change_image(c, button, manager, is_next):
#     user_data = manager.current_context().dialog_data
#     delta = 1 if is_next else -1
#     user_data['image_index'] = (user_data['image_index'] + delta) % len(images)
#     await manager.update({"image": images[user_data['image_index']]})


deck = Window(
    Const("Добро пожаловать!"),
    StaticMedia(path='images/1.webp', type=ContentType.PHOTO),
    Button(Const('Все категории'), id='all_skills', on_click=lambda *a, **k: None),  # noqa: U100
    Row(
        # Button(Const('Влево'), id='left', on_click=lambda c, b, m: change_image(c, b, m, False)),
        # Button(Const('Вправо'), id='right', on_click=lambda c, b, m: change_image(c, b, m, True))
        Button(Const('Влево'), id='left', on_click=lambda *x, **k: None),  # noqa: U100
        Button(Const('Вправо'), id='right', on_click=lambda *x, **k: None)  # noqa: U100
    ),
    Cancel(Const('Назад'), id='back'),
    state=UserDeckStateGroup.deck,
)
