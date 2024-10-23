from telebot.types import Message
from keyboards.inline.inlineButtons import gen_start_markup
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!", reply_markup=gen_start_markup())

