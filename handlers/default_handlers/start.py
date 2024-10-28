from peewee import IntegrityError

from telebot.types import Message, ReplyKeyboardRemove

from database.db_classes import User
from keyboards.inline.inlineButtons import gen_start_markup
from loader import bot
from states.states import BotStates


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.set_state(message.from_user.id, BotStates.default, message.chat.id)
    try:
        User.create(
            user_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
        bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}!")
        bot.send_message(message.from_user.id, f"Я телеграмм-бот <i><u><b>'CARGO'</b></u></i>, и я могу помочь "
                                               f"рассчитать стоимость доставки "
                                               f"Вашего груза, а также заполнить запрос на котировку.В моем функционале "
                                               f"присутствует вся необходимая информация по доставке Вашего груза. "
                                               f"Внимательно ознакомьтесь с разделами "
                                               f"<i><u><b>Главного меню</b></u></i>. Удачи!",
                         reply_markup=gen_start_markup(), parse_mode="HTML")
    except IntegrityError:
        try:
            bot.send_message(message.from_user.id, f"Рад вас снова видеть, {message.from_user.full_name}!",
                             reply_markup=ReplyKeyboardRemove())
            bot.edit_message_reply_markup(message.from_user.id, message.message_id - 1, reply_markup=None)
            bot.send_message(message.from_user.id, f"Добро пожаловать в <i><u><b>Главное меню</b></u></i>.",
                             reply_markup=gen_start_markup(), parse_mode="HTML")
        except:
            bot.send_message(message.from_user.id, f"Рад вас снова видеть, {message.from_user.full_name}!",
                             reply_markup=ReplyKeyboardRemove())
            bot.send_message(message.from_user.id, f"Добро пожаловать в <i><u><b>Главное меню</b></u></i>.",
                             reply_markup=gen_start_markup(), parse_mode="HTML")
