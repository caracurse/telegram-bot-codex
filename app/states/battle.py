from aiogram.fsm.state import State, StatesGroup


class BattleStates(StatesGroup):
    active = State()
