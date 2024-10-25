from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def gen_type_markup():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = KeyboardButton("Посуда")
    but2 = KeyboardButton("Быт.техника")
    but3 = KeyboardButton("Стр.материалы")
    but4 = KeyboardButton("Хоз.товары")
    but5 = KeyboardButton("Обувь/Одежда")
    but6 = KeyboardButton("Игрушки")
    keyboard.row(but1, but2, but3)
    keyboard.row(but4, but5, but6)
    return keyboard


def gen_city_markup():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = KeyboardButton("Москва")
    but2 = KeyboardButton("Алматы")
    keyboard.row(but1, but2)
    return keyboard


def gen_unlicense_markup():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = KeyboardButton("Да")
    but2 = KeyboardButton("Нет")
    keyboard.row(but1, but2)
    return keyboard


def gen_phone_markup() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(text="Telegram", request_contact=True))
    return keyboard


def gen_calculate_markup():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Рассчитать"))
    return keyboard

def gen_send_markup() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Отправить"))
    return keyboard


# def gen_main_markup() -> ReplyKeyboardMarkup:
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton("В главное меню"))
#     return keyboard
