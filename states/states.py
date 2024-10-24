from telebot.handler_backends import StatesGroup, State


class BotCargoStates(StatesGroup):
    type = State()
    invoice = State()
    weight = State()
    volume = State()
    city = State()
    un_license = State()


class BotStates(StatesGroup):
    start = State
    type = State()
    invoice = State()
    weight = State()
    volume = State()
    city = State()
    unlicense = State()
    prequest = State()
    final_calc = State()
