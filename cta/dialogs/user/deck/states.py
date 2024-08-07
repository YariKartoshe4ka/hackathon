from aiogram.fsm.state import State, StatesGroup


class UserDeckStateGroup(StatesGroup):
    deck = State()
