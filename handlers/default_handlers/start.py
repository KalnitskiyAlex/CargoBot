from peewee import IntegrityError

from telebot.types import Message, ReplyKeyboardRemove

from database.db_classes import User
from keyboards.inline.inlineButtons import gen_start_markup
from loader import bot
from states.states import BotStates


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.set_state(message.from_user.id, BotStates.default, message.chat.id)
    bot.edit_message_reply_markup(message.from_user.id, message.message_id - 1, reply_markup=None)
    try:
        User.create(
            user_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
        bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}!",
                         reply_markup=ReplyKeyboardRemove())
        bot.send_message(message.from_user.id, f"Я телеграмм-бот 'CARGO', и я могу помочь рассчитать стоимость доставки "
                                               f"Вашего груза, а также заполнить запрос на котировку.В моем функционале "
                                               f"присутствует вся необходимая информация по доставке Вашего груза. "
                                               f"Внимательно ознакомьтесь с разделами главного меню. Удачи!",
                         reply_markup=gen_start_markup())
    except IntegrityError:
        bot.send_message(message.from_user.id, f"Рад вас снова видеть, {message.from_user.full_name}!",
                         reply_markup=ReplyKeyboardRemove())
        bot.send_message(message.from_user.id, f"Добро пожаловать в главное меню.", reply_markup=gen_start_markup())


