from config import open_weathr_token
import requests
from pprint import pprint
import datetime

def get_wether (city, open_weathr_token):

    code_to_smele = {
        'Clear': "Ясно \U00002600",
        'Clouds': "Облачно \U00002601",
        'Rain': "Дождь \U00002614",
        'Drizzle': "Дождь \U00002614",
        'Thunderstorm': "Гроза \U000026A1",
        'Snow': "Снег \U0001F328",
        'Mist': "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city},&lang=ru&appid={open_weathr_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        name = data['name']
        cur_wether = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']

        weather = data['weather'][0]['main']
        if weather in code_to_smele:
            wd = code_to_smele[weather]
        else:
            wd = 'Посмотри в окно, там непонятно что...'


        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        lenght_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunset'])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f'Погода в городе: {name}\nТемпература: {cur_wether}С° {wd}\nДавление: {pressure} мм.рт.ст.\n'
              f'Влажность: {humidity}\n'
              f'Восход: {sunrise}\nЗакат: {sunset}\nХорошего дня!'
              )

    except Exception as ex:
        print(ex)
        print('Проверьте название города')

def main():
    city = input('Введите город: ')
    get_wether(city, open_weathr_token)

if __name__ == '__main__':
    main()