from telebot.types import CallbackQuery
from keyboards.inline.inlineButtons import gen_main_markup
from loader import bot


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "info")
def cargo_start_calculator(callback_query: CallbackQuery) -> None:
    bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    bot.send_message(callback_query.from_user.id, "Полезная информация которая обязательно пригодится при "
                                                  "перевоке Ваших товаров:\n\n"
                                                  "Адрес нашего склада:\n"
                                                  "КНР, провинция Чжэцзян, город Иу, район И-Ань, улица Хоучдай, дом 35, "
                                                  "Блок 5\n\n"
                                                  "Моб/соцсети:\n"
                                                  "+86 1865 891 59 59\n"
                                                  "+7 995 791 36 05\n\n"
                                                  "E-mail: info@icargo.com.kz\n"
                                                  "Web: icargo.com.kz")
    bot.send_message(callback_query.from_user.id, "Вернуться в главное меню?", reply_markup=gen_main_markup())