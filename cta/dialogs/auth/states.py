from aiogram.fsm.state import State, StatesGroup


class AuthStateGroup(StatesGroup):
    set_username = State()
    set_skills = State()
    set_skill = State()
