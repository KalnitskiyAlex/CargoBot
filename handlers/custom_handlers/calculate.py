from telebot.types import CallbackQuery
from keyboards.inline.inlineButtons import gen_type_markup
from loader import bot
from states.states import BotStates


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "calc")
def cargo_type_calculator(callback_query: CallbackQuery) -> None:
    bot.send_message(callback_query.from_user.id, "Выберите категорию товара: ", reply_markup=gen_type_markup())


# @bot.callback_query_handler(func=lambda callback_query: callback_query.data in ["dishes", "appliances", "materials",
#                                                                                 "household", "clothes", "toys"])
# def cargo_type_calculator(callback_query: CallbackQuery) -> None:
#     bot.send_message(callback_query.from_user.id, "Выберите категорию товара: ", reply_markup=gen_type_markup())
#
#
# @bot.callback_query_handler(func=lambda callback_query: callback_query.data == "new_order")
# def cargo_type_calculator(callback_query: CallbackQuery) -> None:
#     bot.set_state(callback_query.from_user.id, BotStates.type, callback_query.message.from_user.id)
#     bot.send_message(callback_query.from_user.id, "Введите наименование товара: ")
