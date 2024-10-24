from telebot.types import CallbackQuery, Message, ReplyKeyboardRemove
from keyboards.inline.inlineButtons import (gen_calculate_markup, gen_main_markup, gen_start_markup)
from keyboards.reply.replyButtons import gen_type_markup, gen_city_markup, gen_unlicense_markup
from loader import bot
from states.states import BotStates
from utils.misc.price_calculation import price_calculation
from utils.misc.price_selection import price_selection

d = None


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "calc")
def cargo_start_calculator(callback_query: CallbackQuery) -> None:
    global d
    bot.set_state(callback_query.from_user.id, BotStates.type, callback_query.message.chat.id)
    bot.send_message(callback_query.from_user.id, "Категория товара: ", reply_markup=gen_type_markup())


@bot.message_handler(state=BotStates.type)
def cargo_type_calculator(message: Message) -> None:
    try:
        for i_type in ["Посуда", "Быт.техника", "Стр.материалы", "Хоз.товары", "Обувь/Одежда", "Игрушки"]:
            if message.text == i_type:
                with bot.retrieve_data(message.from_user.id) as data:
                    data["type"] = message.text
                break
        else:
            raise ValueError
        bot.set_state(message.from_user.id, BotStates.invoice, message.chat.id)
        bot.send_message(message.from_user.id, "Цена товара в USD: ", reply_markup=ReplyKeyboardRemove())
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Надо выбрать из представленных категорий.")
        bot.send_message(message.from_user.id, "Категория товара: ")


@bot.message_handler(state=BotStates.invoice)
def cargo_invoice_calculator(message: Message) -> None:
    try:
        i_res = message.text.replace(",", ".")
        res = float(i_res)
        if res < 0:
            raise ValueError
        with bot.retrieve_data(message.from_user.id) as data:
            data["invoice"] = res
        bot.set_state(message.from_user.id, BotStates.weight, message.chat.id)
        bot.send_message(message.from_user.id, "Вес брутто товара в кг: ")
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод.")
        bot.send_message(message.from_user.id, "Цена товара в USD: ")

@bot.message_handler(state=BotStates.weight)
def cargo_weight_calculator(message: Message) -> None:
    try:
        i_res = message.text.replace(",", ".")
        res = float(i_res)
        if res < 0:
            raise ValueError
        with bot.retrieve_data(message.from_user.id) as data:
            data["weight"] = res
        bot.set_state(message.from_user.id, BotStates.volume, message.chat.id)
        bot.send_message(message.from_user.id, "Объем товара в м3: ")
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод.")
        bot.send_message(message.from_user.id, "Вес брутто товара в кг: ")


@bot.message_handler(state=BotStates.volume)
def cargo_volume_calculator(message: Message) -> None:
    try:
        i_res = message.text.replace(",", ".")
        res = float(i_res)
        if res < 0:
            raise ValueError
        with bot.retrieve_data(message.from_user.id) as data:
            data["volume"] = res
        bot.set_state(message.from_user.id, BotStates.city, message.chat.id)
        bot.send_message(message.from_user.id, "Город назначения: ", reply_markup=gen_city_markup())
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод.")
        bot.send_message(message.from_user.id, "Объем товара в м3: ")


@bot.message_handler(state=BotStates.city)
def cargo_city_calculator(message: Message) -> None:
    try:
        for city in ["Москва", "Алматы"]:
            if city == message.text:
                with bot.retrieve_data(message.from_user.id) as data:
                    data["city"] = message.text
                break
        else:
            raise ValueError
        bot.set_state(message.from_user.id, BotStates.unlicense, message.chat.id)
        bot.send_message(message.from_user.id, "Товар нелицензионный?",
                         reply_markup=gen_unlicense_markup())
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Надо выбрать из представленных городов.")
        bot.send_message(message.from_user.id, "Город назначения: ")


@bot.message_handler(state=BotStates.unlicense)
def cargo_unlicense_calculator(message: Message) -> None:
    try:
        with bot.retrieve_data(message.from_user.id) as data:
            if message.text == "Да":
                data["unlicense"] = True
            elif message.text == "Нет":
                data["unlicense"] = False
            else:
                raise ValueError
        bot.set_state(message.from_user.id, BotStates.prequest, message.chat.id)
        bot.send_message(message.from_user.id, "Заявка собрана. Для расчета нажмите:",
                         reply_markup=gen_calculate_markup())
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Надо выбрать Да или Нет.")
        bot.send_message(message.from_user.id, "Товар нелицензионный?")




@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "calculate")
def cargo_calculate_calculator(callback_query: CallbackQuery) -> None:
    bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                          text="Результат расчета: ", reply_markup=None)
    with bot.retrieve_data(callback_query.from_user.id) as data:
        # bot.send_message(callback_query.from_user.id, f"type = {data["type"]}")
        # bot.send_message(callback_query.from_user.id, f"weight = {data["weight"]}")
        # bot.send_message(callback_query.from_user.id, f"invoice = {data["invoice"]}")
        # bot.send_message(callback_query.from_user.id, f"volume = {data["volume"]}")
        # bot.send_message(callback_query.from_user.id, f"city = {data["city"]}")
        # bot.send_message(callback_query.from_user.id, f"unlicense = {data["unlicense"]}")
        base_price = price_selection(data["weight"], data["volume"], data["type"])
        price = price_calculation(data["weight"], base_price, data["unlicense"], data["city"], data["invoice"])
    bot.delete_state(callback_query.from_user.id)
    bot.send_message(callback_query.from_user.id, f"Стоимость перевозки товара составляет {round(price, 2)} USD",
                     reply_markup=gen_main_markup())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "main_menu")
def main_menu(callback_query: CallbackQuery) -> None:
    bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                          text="Возврат в главное меню", reply_markup=None)
    bot.send_message(callback_query.from_user.id, f"Добро пожаловать в главное меню. Выберите команду:",
                     reply_markup=gen_start_markup())
