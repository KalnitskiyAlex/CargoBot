from peewee import IntegrityError

from telebot.types import Message

from database.db_classes import User
from keyboards.inline.inlineButtons import gen_start_markup
from loader import bot
from states.states import BotStates


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    try:
        User.create(
            user_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
        bot.set_state(message.from_user.id, BotStates.type, message.chat.id)
        bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}! Я телеграмм-бот 'CARGO', "
                                               f"который поможет  в калькуляции стоимости доставки Вашего груза, "
                                               f"а также поспособствует заполнению заявки.В моем функционале "
                                               f"присутствует вся информация по доставке груза. Внимательно изучите "
                                               f"главное меню. Удачи!", reply_markup=gen_start_markup())
    except IntegrityError:
        bot.send_message(message.from_user.id, f"Рад вас снова видеть, {message.from_user.full_name}!",
                         reply_markup=gen_start_markup())


