from ..database.client import save_user
from ..dialogs.auth.states import AuthStateGroup
from ..dialogs.main.states import MainStateGroup


async def set_username(callback, msg_input, dialog_manager):  # noqa: U100
    # username = message.text
    await dialog_manager.next()


async def set_skills(callback, msg_input, dialog_manager, item_id):  # noqa: U100
    data = dialog_manager.dialog_data
    data['selected_skill'] = item_id

    if 'skills' not in data:
        data['skills'] = {}

    if item_id not in data['skills']:
        data['skills'][item_id] = 0

    data["selected_skill_value"] = data["skills"][item_id]
    await dialog_manager.switch_to(AuthStateGroup.set_skill)


async def increase_skill_value(callback, _, dialog_manager):  # noqa: U100
    data = dialog_manager.dialog_data
    selected_skill = data["selected_skill"]
    value = data["skills"][selected_skill]
    data["selected_skill_value"] = data["skills"][selected_skill] = min(value + 1, 20)


async def decrease_skill_value(callback, _, dialog_manager):  # noqa: U100
    data = dialog_manager.dialog_data
    selected_skill = data["selected_skill"]
    value = data["skills"][selected_skill]
    data["selected_skill_value"] = data["skills"][selected_skill] = max(value - 1, 0)


async def register_user(callback, _, dialog_manager):
    data = dialog_manager.dialog_data
    save_user(callback.from_user.id, data.get('skills', {}))

    await dialog_manager.done()
    await dialog_manager.start(MainStateGroup.main_menu)
