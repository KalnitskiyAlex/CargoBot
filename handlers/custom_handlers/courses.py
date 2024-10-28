from telebot.types import CallbackQuery

from api.courses import get_cbr_rates
from keyboards.inline.inlineButtons import gen_main_markup
from loader import bot


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "courses")
def cargo_start_calculator(callback_query: CallbackQuery) -> None:
    bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    rates = get_cbr_rates()
    bot.send_message(callback_query.from_user.id, "<u><b>Курсы валют</b></u>:", parse_mode="HTML")
    bot.send_message(callback_query.from_user.id, f"Доллар (USD): {rates['USD']} руб.")
    bot.send_message(callback_query.from_user.id, f"Китайский юань (CNY): {rates['CNY']} руб.")
    bot.send_message(callback_query.from_user.id, f"<b>Вернуться в <u><i>Главное меню</i></u></b>?",
                     reply_markup=gen_main_markup(), parse_mode="HTML")
