from telebot.types import CallbackQuery
from keyboards.inline.inlineButtons import gen_main_markup
from loader import bot


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "conditions")
def cargo_start_calculator(callback_query: CallbackQuery) -> None:
    bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    bot.send_message(callback_query.from_user.id, "<u><b>Условия перевозки товаров</b></u>:\n"
                                                  "1. Товар при перевозке подлежит страхованию. "
                                                  "Максимальная страховая стоимость товара не превышает 100 USD/кг.\n"
                                                  "2. Не принимаются к перевозке: контрабандные товары такие как: шерсть, "
                                                  "мех, товары для здоровья, лекарства, чай, жидкости, порошки, "
                                                  "памятные монеты, крышки для бутылок и др. О специальных товарах "
                                                  "необходимо сообщать перевозчику заранее.\n"
                                                  "3. На всем этапе перевозки товаров строго проверяется наличие поддельных "
                                                  "брендов и материалов по профилактике эпидемий, поэтому клиент обязан "
                                                  "предоставлять точные данные по товарам при отгрузке.\n"
                                                  "Пример: название товара, бренд, мужские и женские модели, изображения,"
                                                  " количество мелких деталей, вес, объем, наличие подлинных и "
                                                  "поддельных брендов и т.д., а также упаковочный лист (электронная "
                                                  "версия). Для специальных товаров - описание.\n"
                                                  "4. При непредоставлении точной информации о товаре, ответственность "
                                                  "за последствия ложится на клиента. В этом случае компания "
                                                  "ответственности не несет.\n"
                                                  "5. Накладная на первозку товаров в обязательном порядке "
                                                  "согласовывается с клиентом перед началом перевозки. Возражения и "
                                                  "уточнения принимаются в течение трех рабочих дней с даты "
                                                  "предоставления накладной. При отстутствии комментариев клиента в "
                                                  "течение трех рабочих дней - предполагается, что содержание накладной "
                                                  "верно и изменению не подлежит.", parse_mode='HTML')
    bot.send_message(callback_query.from_user.id, f"<b>Вернуться в <u><i>Главное меню</i></u></b>?",
                     reply_markup=gen_main_markup(), parse_mode='HTML')
