from openpyxl import load_workbook
from pycbrf import ExchangeRates
import telebot
from telebot import apihelper

port = '7777'
usernameProxy = 'tg-id415061327'
passwordProxy = 'vjzTxv7v'
addressProxy = '@socksy.seriyps.ru'

apihelper.proxy = {'https': 'socks5://' + usernameProxy + ':' + passwordProxy + addressProxy + ':' + port}

TOKEN = '638610225:AAEoPelXhzUC11J11x8L9bBHbjoGPKj9zXk'

bot = telebot.TeleBot(TOKEN)


def indexing(search):
    """Поиск нужных позиций."""

    file = 'db_1.xlsx'
    wb1 = load_workbook(filename=file)
    ws1 = wb1['price']
    rates = ExchangeRates('2019-06-21', locale_en=True)
    curse_eur = rates['EUR'].value

    # Поиск по ключам
    search = search.split()

    number_of_index = 0
    name_of_search = []
    cost_of_search = []
    date_of_search = []

    for row_i in range(ws1.max_row - 1):
        tru_or_not_tru = []
        for search_i in search:
            tru_or_not_tru.append(search_i in ws1['w' + str(row_i + 2)].value)

        if not False in tru_or_not_tru:
            number_of_index += 1
            name_of_search.append('№' + str(number_of_index) + '. ' + str(ws1['f' + str(row_i + 2)].value))
            cost_of_search.append('Стоимость - ' + str(ws1['j' + str(row_i + 2)].value) + ' EUR')
            date_of_search.append('Срок поставки - ' + str(ws1['q' + str(row_i + 2)].value) + ' дней до 3М в России')

    return name_of_search, cost_of_search, date_of_search, number_of_index


@bot.message_handler(content_types=['text'])
def send_echo(message):

    answer = indexing(message.text)

    if answer[3] > 3:
        bot.send_message(message.chat.id, 'Найдено более 3 наименований')
    else:
        for i in range(len(answer[0])):
            bot.send_message(message.chat.id, answer[0][i])
            bot.send_message(message.chat.id, answer[1][i])
            bot.send_message(message.chat.id, answer[2][i])


bot.polling(none_stop=True)
