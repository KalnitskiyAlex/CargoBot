from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_start_markup():
    keyboard = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("Калькулятор", callback_data="calc")
    but2 = InlineKeyboardButton("Подать заявку", callback_data="new_order")
    keyboard.row(but1, but2)
    return keyboard


def gen_type_markup():
    keyboard = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("Посуда", callback_data="dishes")
    but2 = InlineKeyboardButton("Быт.техника", callback_data="appliances")
    but3 = InlineKeyboardButton("Стр.материалы", callback_data="materials")
    but4 = InlineKeyboardButton("Хоз.товары", callback_data="household")
    but5 = InlineKeyboardButton("Обувь/Одежда", callback_data="clothes")
    but6 = InlineKeyboardButton("Игрушки", callback_data="toys")
    keyboard.row(but1, but2, but3)
    keyboard.row(but4, but5, but6)
    return keyboard


def gen_city_markup():
    keyboard = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("Москва", callback_data="moscow_city")
    but2 = InlineKeyboardButton("Алматы", callback_data="almaty_city")
    keyboard.row(but1, but2)
    return keyboard


def gen_unlicense_markup():
    keyboard = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("Да", callback_data="yes")
    but2 = InlineKeyboardButton("Нет", callback_data="no")
    keyboard.row(but1, but2)
    return keyboard
