from telebot.types import Message, ReplyKeyboardRemove
from config_data.config import DEFAULT_COMMANDS
from keyboards.inline.inlineButtons import gen_main_markup
from loader import bot
from states.states import BotStates


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    bot.set_state(message.from_user.id, BotStates.default, message.chat.id)
    bot.edit_message_reply_markup(message.from_user.id, message.message_id - 1, reply_markup=None)
    bot.send_message(message.from_user.id, f"Меню стандартных команд бота:",
                     reply_markup=ReplyKeyboardRemove())
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.send_message(message.from_user.id, "\n".join(text))
    bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=gen_main_markup())

