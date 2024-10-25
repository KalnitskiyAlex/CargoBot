from telebot.types import CallbackQuery, Message, ReplyKeyboardRemove

from database.db_classes import Request
from keyboards.inline.inlineButtons import (gen_calculate_markup, gen_main_markup, gen_start_markup, gen_send_markup)
from keyboards.reply.replyButtons import gen_city_markup, gen_unlicense_markup
from loader import bot
from states.states import BotRequestStates
from datetime import datetime


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "new_order")
def cargo_start_calculator(callback_query: CallbackQuery) -> None:
    bot.send_message(callback_query.from_user.id, "Вы находитесь в меню 'Заявка на перевозку товара'. "
                                                  "Прошу Вас ответственно подойти к заполнению разделов заявки.")
    bot.set_state(callback_query.from_user.id, BotRequestStates.req_type, callback_query.message.chat.id)
    bot.send_message(callback_query.from_user.id, "Наименование товара: ")


@bot.message_handler(state=BotRequestStates.req_type)
def cargo_type_calculator(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id) as data:
        data["type"] = message.text
    bot.set_state(message.from_user.id, BotRequestStates.req_invoice, message.chat.id)
    bot.send_message(message.from_user.id, "Цена товара в USD: ")


@bot.message_handler(state=BotRequestStates.req_invoice)
def cargo_invoice_calculator(message: Message) -> None:
    try:
        i_res = message.text.replace(",", ".")
        res = float(i_res)
        if res < 0:
            raise ValueError
        with bot.retrieve_data(message.from_user.id) as data:
            data["invoice"] = res
        bot.set_state(message.from_user.id, BotRequestStates.req_weight, message.chat.id)
        bot.send_message(message.from_user.id, "Вес брутто товара в кг: ")
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод.")
        bot.send_message(message.from_user.id, "Цена товара в USD: ")


@bot.message_handler(state=BotRequestStates.req_weight)
def cargo_weight_calculator(message: Message) -> None:
    try:
        i_res = message.text.replace(",", ".")
        res = float(i_res)
        if res < 0:
            raise ValueError
        with bot.retrieve_data(message.from_user.id) as data:
            data["weight"] = res
        bot.set_state(message.from_user.id, BotRequestStates.req_volume, message.chat.id)
        bot.send_message(message.from_user.id, "Объем товара в м3: ")
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод.")
        bot.send_message(message.from_user.id, "Вес брутто товара в кг: ")


@bot.message_handler(state=BotRequestStates.req_volume)
def cargo_volume_calculator(message: Message) -> None:
    try:
        i_res = message.text.replace(",", ".")
        res = float(i_res)
        if res < 0:
            raise ValueError
        with bot.retrieve_data(message.from_user.id) as data:
            data["volume"] = res
        bot.set_state(message.from_user.id, BotRequestStates.req_city, message.chat.id)
        bot.send_message(message.from_user.id, "Город назначения: ", reply_markup=gen_city_markup())
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод.")
        bot.send_message(message.from_user.id, "Объем товара в м3: ")


@bot.message_handler(state=BotRequestStates.req_city)
def cargo_city_calculator(message: Message) -> None:
    try:
        for city in ["Москва", "Алматы"]:
            if city == message.text:
                with bot.retrieve_data(message.from_user.id) as data:
                    data["city"] = message.text
                break
        else:
            raise ValueError
        bot.set_state(message.from_user.id, BotRequestStates.req_unlicense, message.chat.id)
        bot.send_message(message.from_user.id, "Товар нелицензионный?",
                         reply_markup=gen_unlicense_markup())
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Надо выбрать из представленных городов.")
        bot.send_message(message.from_user.id, "Город назначения: ")


@bot.message_handler(state=BotRequestStates.req_unlicense)
def cargo_unlicense_calculator(message: Message) -> None:
    try:
        with bot.retrieve_data(message.from_user.id) as data:
            if message.text == "Да":
                data["unlicense"] = True
            elif message.text == "Нет":
                data["unlicense"] = False
            else:
                raise ValueError
        bot.set_state(message.from_user.id, BotRequestStates.req_send, message.chat.id)
        bot.send_message(message.from_user.id, "Заявка собрана.",
                         reply_markup=gen_send_markup())
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Надо выбрать Да или Нет.")
        bot.send_message(message.from_user.id, "Товар нелицензионный?")


@bot.message_handler(state=BotRequestStates.req_send)
def cargo_unlicense_calculator(message: Message) -> None:
    try:
        if message.text:
            raise ValueError
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Выберите кнопку")


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "send")
def cargo_calculate_calculator(callback_query: CallbackQuery) -> None:
    with bot.retrieve_data(callback_query.from_user.id) as data:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        type, weight, invoice, volume, city, unlicense = data["type"], data["weight"], data["invoice"], data["volume"], \
        data["city"], data["unlicense"]
    Request.create(
        user=callback_query.from_user.full_name,
        date=now,
        type=type,
        invoice=invoice,
        weight=weight,
        volume=volume,
        city=city,
        unlicense=unlicense
    )
    bot.delete_state(callback_query.from_user.id)
    bot.send_message(callback_query.from_user.id, f"{callback_query.from_user.full_name}|{now}|{data["type"]}|"
                                                  f"{data["invoice"]}|{data["weight"]}|{data["volume"]}|{data["city"]}|"
                                                  f"{data["unlicense"]}")


# @bot.callback_query_handler(func=lambda callback_query: callback_query.data == "main_menu")
# def main_menu(callback_query: CallbackQuery) -> None:
#     bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
#                           text="Возврат в главное меню", reply_markup=None)
#     bot.send_message(callback_query.from_user.id, f"Добро пожаловать в главное меню. Выберите команду:",
#                      reply_markup=gen_start_markup())
