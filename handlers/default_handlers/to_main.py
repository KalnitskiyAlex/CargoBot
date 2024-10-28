from telebot.types import Message, CallbackQuery
from keyboards.inline.inlineButtons import gen_start_markup
from loader import bot
from states.states import BotStates


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "to_main")
def to_main_menu(callback_query: CallbackQuery) -> None:
    bot.set_state(callback_query.from_user.id, BotStates.default, callback_query.message.chat.id)
    bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    bot.send_message(callback_query.from_user.id, f"Добро пожаловать в <i><u><b>Главное меню</b></u></i>. "
                                                  f"Выберите команду:", reply_markup=gen_start_markup(),
                     parse_mode="HTML")


@bot.message_handler(state=BotStates.default)
def cargo_telegram_state_request(message: Message) -> None:
    try:
        if message.text:
            raise ValueError
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Выберите кнопку или команду.")

