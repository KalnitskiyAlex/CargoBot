from telebot.types import CallbackQuery, Message, ReplyKeyboardRemove

from config_data.config import MANAGER_ID
from database.db_classes import Request
from keyboards.inline.inlineButtons import gen_main_markup
from keyboards.reply.replyButtons import gen_city_markup, gen_unlicense_markup, gen_send_markup, gen_phone_markup
from loader import bot
from states.states import BotRequestStates, BotStates
from datetime import datetime


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "new_order")
def cargo_start_request(callback_query: CallbackQuery) -> None:
    bot.send_message(callback_query.from_user.id, "Вы формируете Заявку на перевозку груза. "
                                                  "Прошу Вас ответственно подойти к заполнению разделов заявки.")
    bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    bot.set_state(callback_query.from_user.id, BotRequestStates.req_type, callback_query.message.chat.id)
    bot.send_message(callback_query.from_user.id, "Наименование товара: ")


@bot.message_handler(state=BotRequestStates.req_type)
def cargo_type_request(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id) as data:
        data["type"] = message.text
    bot.set_state(message.from_user.id, BotRequestStates.req_invoice, message.chat.id)
    bot.send_message(message.from_user.id, "Цена товара в USD: ")


@bot.message_handler(state=BotRequestStates.req_invoice)
def cargo_invoice_request(message: Message) -> None:
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
def cargo_weight_request(message: Message) -> None:
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
def cargo_volume_request(message: Message) -> None:
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
def cargo_city_request(message: Message) -> None:
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
def cargo_unlicense_request(message: Message) -> None:
    try:
        with bot.retrieve_data(message.from_user.id) as data:
            if message.text == "Да":
                data["unlicense"] = True
            elif message.text == "Нет":
                data["unlicense"] = False
            else:
                raise ValueError
        bot.set_state(message.from_user.id, BotRequestStates.telegram, message.chat.id)
        bot.send_message(message.from_user.id, "Контакт для связи: ",
                         reply_markup=gen_phone_markup())
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Надо выбрать Да или Нет.")
        bot.send_message(message.from_user.id, "Товар нелицензионный?")

@bot.message_handler(state=BotRequestStates.telegram)
def cargo_telegram_state_request(message: Message) -> None:
    try:
        if message.text:
            raise ValueError
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Выберите кнопку")
        bot.send_message(message.from_user.id, "Контакт для связи: ")
@bot.message_handler(content_types=['contact'])
def cargo_telegram_request(message: Message):
    telegram = message.contact.phone_number
    with bot.retrieve_data(message.from_user.id) as data:
        data["phone_number"] = telegram
    bot.set_state(message.from_user.id, BotRequestStates.req_send, message.chat.id)
    bot.send_message(message.from_user.id, f"Заявка создана.", reply_markup=gen_send_markup())


@bot.message_handler(state=BotRequestStates.req_send)
def cargo_send_request(message: Message) -> None:
    try:
        if message.text == "Отправить":
            with (bot.retrieve_data(message.from_user.id) as data):
                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                type, weight, invoice, volume, city, phone_number = data["type"], data["weight"], data["invoice"], \
                data["volume"], data["city"], data["phone_number"]
                if data["unlicense"]:
                    unlicense = "Да"
                else:
                    unlicense = "Нет"
            Request.create(
                user=message.from_user.full_name,
                date=now,
                type=type,
                invoice=invoice,
                weight=weight,
                volume=volume,
                city=city,
                unlicense=unlicense,
                phone_number=phone_number
            )
            bot.set_state(message.from_user.id, BotStates.default, message.chat.id)
            bot.send_message(message.from_user.id, f"Заявка отправлена на расчет.", reply_markup=ReplyKeyboardRemove())
            bot.send_message(MANAGER_ID, f"Заказчик: {message.from_user.full_name}\nКонтактный номер: "
                                                   f"{data["phone_number"]}\nДата заявки: {now}\nПараметры заявки\n"
                                                   f"Тип товара: {data["type"]}\nСтоимость товара по инвойсу, USD: "
                                                   f"{data["invoice"]}\nВес брутто, кг: {data["weight"]}\nОбъём, м3: "
                                                   f"{data["volume"]}\nГород назначения: {data["city"]}\n"
                                                   f"Товар нелицензионный: {data["unlicense"]}")
            bot.send_message(message.from_user.id, f"Для возврата в главное меню нажмите:",
                             reply_markup=gen_main_markup())
        else:
            raise ValueError
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Выберите кнопку")



