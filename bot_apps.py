import datetime
import locale
import requests
from os import getenv
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from keys import key_city


API_TOKEN = getenv('API_WEATHER')  # your token open weather
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

bot = Bot(token=getenv('API_BOT_WEATHER'))  # your token bot
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Выбери в меню город\n'
                        'или введи требуемый для отображения сводки погоды!', reply_markup=key_city)


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={API_TOKEN}&units=metric&lang=ru")
        data = r.json()

        city_name = data['name']
        dt = datetime.datetime.fromtimestamp(data['dt']).strftime('%A %d %B')
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'], 1)
        feels_like = round(data['main']['feels_like'], 1)
        humidity = data['main']['humidity']
        pressure = round((data['main']['pressure']) * 0.750)
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        long_day = (datetime.datetime.fromtimestamp(data['sys']['sunset'])) - (
            datetime.datetime.fromtimestamp(data['sys']['sunrise']))

        await message.reply(f'Сегодня: {dt}\n'
                            f'В городе {city_name} сейчас {weather}\n'
                            f'Температура воздуха: {temperature} С°\n'
                            f'Ощущается как: {feels_like} С°\n'
                            f'Влажность воздуха: {humidity} % \n'
                            f'Давление: {pressure} мм рт.ст.\n'
                            f'Ветер: {wind} м/с\n'
                            f'Восход солнца в {sunrise}\n'
                            f'Закат солнца в {sunset}\n'
                            f'Световой день: {long_day}\n')

    except KeyError:
        await message.reply('Проверьте название города!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
