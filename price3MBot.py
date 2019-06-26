from openpyxl import load_workbook
from pycbrf import ExchangeRates
import telebot
from telebot import apihelper
from telebot import types

port = '7777'
usernameProxy = 'tg-id415061327'
passwordProxy = 'vjzTxv7v'
addressProxy = '@socksy.seriyps.ru'

apihelper.proxy = {'https': 'socks5://' + usernameProxy + ':' + passwordProxy + addressProxy + ':' + port}

TOKEN = '638610225:AAEoPelXhzUC11J11x8L9bBHbjoGPKj9zXk'

bot = telebot.TeleBot(TOKEN)


# Поиск по ключам
def indexing(search):
    """Поиск нужных позиций."""

    file = 'db_1.xlsx'
    wb1 = load_workbook(filename=file)
    ws1 = wb1['price']
    rates = ExchangeRates('2019-06-25', locale_en=True)

    # Поиск по ключам
    search = search.lower()
    search = search.split(' ')

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

            if ws1['m' + str(row_i + 2)].value == 'EUR':
                curse_eur = float(rates['EUR'].value)
            else:
                curse_eur = 1

            name_of_search.append('№' + str(number_of_index) + '. ' + str(ws1['f' + str(row_i + 2)].value))

            cost_tmp = str(ws1['j' + str(row_i + 2)].value).split(',')
            cost_tmp = round(float(cost_tmp[0]) * 1.2 * curse_eur, 2)
            cost_of_search.append('Стоимость - {0} руб. с НДС или {1} EUR Без НДС'.format(str(cost_tmp), ws1['j' +
                                                                                                             str(
                                                                                                                 row_i + 2)].value))

            date_of_search.append('Статус товара на складе 3М Россия - ' + str(ws1['l' + str(row_i + 2)].value))

    return name_of_search, cost_of_search, date_of_search, number_of_index


# Команды '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    bot.send_message(message.chat.id, '''Правила поиска по прайсу : 1. Регистр не учитывается. 2. Поииск идет по 
    ключевым словам, которые нужно вводить через пробел. ''')


# Поиск по прайсу
@bot.message_handler(content_types=['text'])
def send_search_id(message):
    answer = indexing(message.text)

    if answer[3] > 3:
        bot.send_message(message.chat.id, 'Найдено более 3 наименований')
    elif answer[3] == 0:
        bot.send_message(message.chat.id, 'Не найдено ни одной позиции')
    else:
        for i in range(len(answer[0])):
            bot.send_message(message.chat.id, answer[0][i])
            bot.send_message(message.chat.id, answer[1][i])
            bot.send_message(message.chat.id, answer[2][i])

    # keyboard = types.InlineKeyboardMarkup()
    # url_button = types.InlineKeyboardButton(text='Перейти на Тэйплайн', url='http://www.tapeline.ru/')
    # keyboard.add(url_button)
    # bot.send_message(message.chat.id, 'Дальнейший выбор', reply_markup=keyboard)


bot.polling(none_stop=True)
