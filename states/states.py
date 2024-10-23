from telebot.handler_backends import StatesGroup, State


class BotCargoStates(StatesGroup):
    type = State()
    invoice = State()
    weight = State()
    volume = State()
    city = State()
    un_license = State()


class BotStates(StatesGroup):
    type = State()
    invoice = State()
    weight= State()
    volume = State()
    city = State()
    un_license = State()
