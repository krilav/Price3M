import  datetime
from datetime import timedelta
import time
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


@bot.message_handler(content_types=["text"])
def any_msg(message):
    date_curse = datetime.date.today() - timedelta(1)

    bot.send_message(message.chat.id, '''дата время  :  {} '''.format(date_curse))


bot.polling(none_stop=True)
