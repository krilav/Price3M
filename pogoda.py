# pagoda

import pyowm
import time

owm = pyowm.OWM('7215c81c62b322b41e0aa0eb1843c5d4', language='ru')

place = 'Красноярск'  # input('Введите город : ')

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')['temp']
speed = w.get_wind()['speed']
humidity = w.get_humidity()
city_time = w.get_reference_time()

print('Температура в городе ' + place + ' сейчас ' + str(temp) + ' цельсия')
print('Влажность воздуха ' + str(humidity) + "%")
print('Скорость ветра в городе ' + place + ' сейчас ' + str(speed) + " м/с")
print('На небе ' + w.get_detailed_status())

# print(w)

print(time.ctime(city_time))
