from telebot.handler_backends import StatesGroup, State


class BotRequestStates(StatesGroup):
    req_type = State()
    req_invoice = State()
    req_weight = State()
    req_volume = State()
    req_city = State()
    req_unlicense = State()
    req_send = State()



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
