from telebot.types import Message
from loader import bot
from states.states import BotStates

@bot.message_handler(state=BotStates.default)
def cargo_telegram_state_request(message: Message) -> None:
    try:
        if message.text:
            raise ValueError
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Выберите кнопку или команду.")

