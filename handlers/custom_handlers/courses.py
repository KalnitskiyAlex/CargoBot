from telebot.types import CallbackQuery

from api.courses import get_cbr_rates
from keyboards.inline.inlineButtons import gen_main_markup
from loader import bot



@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "courses")
def cargo_start_calculator(callback_query: CallbackQuery) -> None:
    bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    rates = get_cbr_rates()
    bot.send_message(callback_query.from_user.id, "Курсы валют:")
    bot.send_message(callback_query.from_user.id, f"Доллар (USD): {round(rates['USD'], 2)} руб.")
    bot.send_message(callback_query.from_user.id, f"Китайский юань (CNY): {round(rates['CNY'])} руб.")
    bot.send_message(callback_query.from_user.id, "Вернуться в главное меню?",
                     reply_markup=gen_main_markup())