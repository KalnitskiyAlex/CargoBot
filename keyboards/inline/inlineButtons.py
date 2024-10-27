from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_start_markup():
    keyboard = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("Калькулятор", callback_data="calc")
    but2 = InlineKeyboardButton("Запросить котировку", callback_data="new_order")
    but3 = InlineKeyboardButton("Условия", callback_data="conditions")
    but4 = InlineKeyboardButton("Информация", callback_data="info")
    but5 = InlineKeyboardButton("Курсы ЦБРФ", callback_data="courses")
    keyboard.row(but1, but2)
    keyboard.row(but3, but4)
    keyboard.row(but5)
    return keyboard


def gen_main_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("В главное меню", callback_data="to_main"))
    return keyboard






