from telebot.types import CallbackQuery, Message
from keyboards.inline.inlineButtons import (gen_type_markup, gen_city_markup, gen_unlicense_markup,
                                            gen_calculate_markup, gen_main_markup, gen_start_markup)
from loader import bot
from states.states import BotStates
from utils.misc.price_calculation import price_calculation
from utils.misc.price_selection import price_selection


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "calc")
def cargo_start_calculator(callback_query: CallbackQuery) -> None:
    bot.set_state(callback_query.from_user.id, BotStates.type, callback_query.message.chat.id)
    bot.send_message(callback_query.from_user.id, "Выберите категорию товара: ", reply_markup=gen_type_markup())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data in ["dishes", "appliances", "materials",
                                                                                "household", "clothes", "toys"])
def cargo_type_calculator(callback_query: CallbackQuery) -> None:
    bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                          text="Категория товара выбрана", reply_markup=None)
    with bot.retrieve_data(callback_query.from_user.id) as data:
        data["type"] = callback_query.data
    bot.set_state(callback_query.from_user.id, BotStates.invoice, callback_query.message.chat.id)
    bot.send_message(callback_query.from_user.id, "Укажите цену товара в USD: ")


@bot.message_handler(state=BotStates.invoice)
def cargo_invoice_calculator(message: Message) -> None:
    try:
        res = float(message.text)
        if res < 0:
            raise ValueError
        with bot.retrieve_data(message.from_user.id) as data:
            data["invoice"] = res
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id - 1,
                              text="Цена товара указана", reply_markup=None)
        bot.set_state(message.from_user.id, BotStates.weight, message.chat.id)
        bot.send_message(message.from_user.id, "Укажите вес брутто в кг: ")
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Укажите цену товара в USD: ")


@bot.message_handler(state=BotStates.weight)
def cargo_weight_calculator(message: Message) -> None:
    try:
        res = float(message.text)
        if res < 0:
            raise ValueError
        with bot.retrieve_data(message.from_user.id) as data:
            data["weight"] = message.text
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id - 1,
                              text="Вес товара указан", reply_markup=None)
        bot.set_state(message.from_user.id, BotStates.volume, message.chat.id)
        bot.send_message(message.from_user.id, "Укажите объем в м3: ")
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Укажите вес брутто в кг: ")


@bot.message_handler(state=BotStates.volume)
def cargo_volume_calculator(message: Message) -> None:
    try:
        res = float(message.text)
        if res < 0:
            raise ValueError
        with bot.retrieve_data(message.from_user.id) as data:
            data["volume"] = message.text
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id - 1,
                              text="Объем товара указан", reply_markup=None)
        bot.set_state(message.from_user.id, BotStates.city, message.chat.id)
        bot.send_message(message.from_user.id, "Выберите город назначения: ", reply_markup=gen_city_markup())
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Укажите объем в м3: ")


@bot.callback_query_handler(func=lambda callback_query: callback_query.data in ["moscow_city", "almaty_city"])
def cargo_city_calculator(callback_query: CallbackQuery) -> None:
    bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                          text="Город назначения указан", reply_markup=None)
    with bot.retrieve_data(callback_query.from_user.id) as data:
        data["city"] = callback_query.data
    bot.set_state(callback_query.from_user.id, BotStates.un_license, callback_query.message.chat.id)
    bot.send_message(callback_query.from_user.id, "Является ли товар нелицензионным?",
                     reply_markup=gen_unlicense_markup())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data in ["yes", "no"])
def cargo_unlicense_calculator(callback_query: CallbackQuery) -> None:
    bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                          text="Информация о нелицензионности получена", reply_markup=None)
    with bot.retrieve_data(callback_query.from_user.id) as data:
        if callback_query.data == "yes":
            data["unlicense"] = True
        elif callback_query.data == "no":
            data["unlicense"] = False
    bot.set_state(callback_query.from_user.id, BotStates.prequest, callback_query.message.chat.id)
    bot.send_message(callback_query.from_user.id, "Заявка собрана. Для расчета нажмите:",
                     reply_markup=gen_calculate_markup())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "calculate")
def cargo_calculate_calculator(callback_query: CallbackQuery) -> None:
    bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                          text="Результат расчета: ", reply_markup=None)
    with bot.retrieve_data(callback_query.from_user.id) as data:
        base_price = price_selection(data["weight"], data["volume"], data["type"])
        price = price_calculation(data["weight"], base_price, data["unlicense"], data["city"], data["invoice"])
    bot.delete_state(callback_query.from_user.id)
    bot.send_message(callback_query.from_user.id, f"Стоимость перевозки товара составляет {price} USD")
    bot.send_message(callback_query.from_user.id, f"Вернуться в главное меню? Нажмите: ",
                     reply_markup=gen_main_markup())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "main_menu")
def main_menu(callback_query: CallbackQuery) -> None:
    bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                          text="Возврат в главное меню", reply_markup=None)
    bot.send_message(callback_query.from_user.id, f"Добро пожаловать в главное меню. Выберите команду:",
                     reply_markup=gen_start_markup())