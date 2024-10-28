from telebot.types import Message, ReplyKeyboardRemove
from config_data.config import DEFAULT_COMMANDS
from keyboards.inline.inlineButtons import gen_main_markup
from loader import bot
from states.states import BotStates


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    try:
        bot.set_state(message.from_user.id, BotStates.default, message.chat.id)
        bot.edit_message_reply_markup(message.from_user.id, message.message_id - 1, reply_markup=None)
        bot.send_message(message.from_user.id, f"<u><b>Меню стандартных команд бота:</b></u>",
                         reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')
        text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
        bot.send_message(message.from_user.id, "\n".join(text))
        bot.send_message(message.from_user.id, "<b>Вернуться в главное меню?</b>",
                         reply_markup=gen_main_markup(), parse_mode='HTML')
    except:
        bot.set_state(message.from_user.id, BotStates.default, message.chat.id)
        bot.send_message(message.from_user.id, f"<u><b>Меню стандартных команд бота:</b></u>",
                         reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')
        text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
        bot.send_message(message.from_user.id, "\n".join(text))
        bot.send_message(message.from_user.id, f"<b>Вернуться в <u><i>Главное меню</i></u></b>?",
                         reply_markup=gen_main_markup(), parse_mode='HTML')
