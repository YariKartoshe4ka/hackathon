from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import (Button, Cancel, Checkbox, Row,
                                        ScrollingGroup, Select, SwitchTo)
from aiogram_dialog.widgets.text import Const, Format

from ...handlers.auth import *
from .states import AuthStateGroup

set_username = Window(
    Const("Банер туда сюда добро пожаловать мы бот сделанный на коленках, вам необходимо пройти регулярно. ВВедите Ваше имя!"),
    MessageInput(set_username),
    state=AuthStateGroup.set_username,
)

set_skills = Window(
    Const("huihuihuihuhi"),
    *[Select(
        Format("{item}"),
        item_id_getter=lambda x: x,
        items=row,
        id="selected_skill",
        on_click=set_skills
    ) for row in [['Pwn', 'Reverse', 'Web', 'Crypto'], ['Forensic', 'PPC', 'Pentest']]],
    # SwitchTo(Const("Готово"), id="done", state=AuthStateGroup.auth),
    state=AuthStateGroup.set_skills
)

set_skill = Window(
    Format("Ваше текущее значение навыка {dialog_data[selected_skill]}: {dialog_data[selected_skill_value]}"),
    Row(
        Button(Const('-'), id="increase", on_click=decrease_skill_value),
        Button(Format("{dialog_data[selected_skill_value]}"), id="skill"),
        Button(Const('+'), id="decrease", on_click=increase_skill_value)
    ),
    SwitchTo(Const('Назад'), id="back", state=AuthStateGroup.set_skills),
    MessageInput(lambda x: None),
    state=AuthStateGroup.set_skill
)
