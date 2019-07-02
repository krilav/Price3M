from telebot import types
import math
import pyowm
import telebot
from telebot import apihelper

owm = pyowm.OWM('7215c81c62b322b41e0aa0eb1843c5d4', language='ru')

port = '7777'
usernameProxy = 'tg-id415061327'
passwordProxy = 'vjzTxv7v'
addressProxy = '@socksy.seriyps.ru'

apihelper.proxy = {'https': 'socks5://' + usernameProxy + ':' + passwordProxy + addressProxy + ':' + port}

# TOKEN = '638610225:AAEoPelXhzUC11J11x8L9bBHbjoGPKj9zXk'
TOKEN = "842039603:AAFy4Cd_mWZSyjFEQGcUgI0uYP87ZrQy1pQ"


bot = telebot.TeleBot(TOKEN)


# кнопки вызывающие действия
@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
    callback_button2 = types.InlineKeyboardButton(text="Нажми меня2", callback_data="test2")
    keyboard.add(callback_button, callback_button2)
    bot.send_message(message.chat.id, "Я сообщение", reply_markup=keyboard)


# обработчик (кнопки вызывающие действия)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")

        elif call.data == "test2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Пыщь2")


bot.polling(none_stop=True)
