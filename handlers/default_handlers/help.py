from telebot.types import Message, ReplyKeyboardRemove
from config_data.config import DEFAULT_COMMANDS
from keyboards.inline.inlineButtons import gen_main_markup
from loader import bot
from states.states import BotStates


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    bot.set_state(message.from_user.id, BotStates.default, message.chat.id)
    bot.send_message(message.from_user.id, f"Меню стандартных команд бота:",
                     reply_markup=ReplyKeyboardRemove())
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))
    bot.send_message(message.from_user.id, f"Для возврата в главное меню нажмите:",
                     reply_markup=gen_main_markup())
