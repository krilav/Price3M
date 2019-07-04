import datetime
import time
import math
import telebot

from datetime import timedelta
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import apihelper


port = '7777'
usernameProxy = 'tg-id415061327'
passwordProxy = 'vjzTxv7v'
addressProxy = '@socksy.seriyps.ru'

apihelper.proxy = {'https': 'socks5://' + usernameProxy + ':' + passwordProxy + addressProxy + ':' + port}

# TOKEN = '638610225:AAEoPelXhzUC11J11x8L9bBHbjoGPKj9zXk'
TOKEN = "842039603:AAFy4Cd_mWZSyjFEQGcUgI0uYP87ZrQy1pQ"

bot = telebot.TeleBot(TOKEN)


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Answer is No")


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())


bot.polling(none_stop=True)
