from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_start_markup():
    keyboard = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("Калькулятор", callback_data="calc")
    but2 = InlineKeyboardButton("Подать заявку", callback_data="new_order")
    keyboard.row(but1, but2)
    return keyboard


def gen_city_markup():
    keyboard = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("Москва", callback_data="moscow_city")
    but2 = InlineKeyboardButton("Алматы", callback_data="almaty_city")
    keyboard.row(but1, but2)
    return keyboard


def gen_calculate_markup():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Рассчитать", callback_data="calculate"))
    return keyboard


def gen_main_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Главное меню", callback_data="main_menu"))
    return keyboard


def gen_send_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Отправить", callback_data="send"))
    return keyboard
