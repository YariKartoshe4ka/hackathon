from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Row, Select, SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from ...handlers.auth import (decrease_skill_value, increase_skill_value,
                              register_user, set_skills, set_username)
from .states import AuthStateGroup

set_username = Window(
    Const(
        'Добро пожаловать в бота "LetoCTF собери их всех"\n\n'
        'В нашем мире не так давно начали появляться удивительные ctf-ры! Люди с удивительными '
        'скилами, обожающие бросать вызов самым заковыристым загадкам окружают нас. Пора '
        'использовать нетворкинг и законектится с ними!'
    ),
    MessageInput(set_username),
    state=AuthStateGroup.set_username,
)


set_skills = Window(
    Const(
        'Ты сделал правильный выбор! Теперь пора узнать кто ты.\n'
        'Тебе даны 30 очков характеристик, распредели их в соответствии с твоими навыками'
    ),
    *[Select(
        Format("{item}"),
        item_id_getter=lambda x: x,
        items=row,
        id="selected_skill",
        on_click=set_skills
    ) for row in [['Pwn', 'Reverse', 'Web', 'Crypto'], ['Forensic', 'PPC', 'Pentest']]],
    Button(Const("Готово"), id="done", on_click=register_user),
    state=AuthStateGroup.set_skills
)

set_skill = Window(
    Format(
        'Ваше текущее значение навыка {dialog_data[selected_skill]}: '
        '{dialog_data[selected_skill_value]}'
    ),
    Row(
        Button(Const('-'), id="increase", on_click=decrease_skill_value),
        Button(Format("{dialog_data[selected_skill_value]}"), id="skill"),
        Button(Const('+'), id="decrease", on_click=increase_skill_value)
    ),
    SwitchTo(Const('Назад'), id="back", state=AuthStateGroup.set_skills),
    state=AuthStateGroup.set_skill
)
