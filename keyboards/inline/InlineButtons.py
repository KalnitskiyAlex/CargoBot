from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_start_markup():
    keyboard = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("Калькулятор", callback_data="price")
    but2 = InlineKeyboardButton("Подать заявку", callback_data="calculate")
    keyboard.row(but1, but2)
    return keyboard
