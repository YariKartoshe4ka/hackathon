from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from ..dialogs.auth.states import AuthStateGroup


async def set_username(message, _, dialog_manager):
    username = message.text
    await dialog_manager.next()

async def set_skills(callback, _, dialog_manager, item_id):
    data = dialog_manager.dialog_data
    data['selected_skill'] = item_id

    if 'skills' not in data:
        data['skills'] = {}

    if item_id not in data['skills']:
        data['skills'][item_id] = 0

    data["selected_skill_value"] = data["skills"][item_id]
    await dialog_manager.switch_to(AuthStateGroup.set_skill)

async def increase_skill_value(callback, _, dialog_manager):
    data = dialog_manager.dialog_data
    selected_skill = data["selected_skill"]
    value = data["skills"][selected_skill]
    data["selected_skill_value"] = data["skills"][selected_skill] = min(value + 1, 20)

async def decrease_skill_value(callback, _, dialog_manager):
    data = dialog_manager.dialog_data
    selected_skill = data["selected_skill"]
    value = data["skills"][selected_skill]
    data["selected_skill_value"] = data["skills"][selected_skill] = max(value - 1, 0)