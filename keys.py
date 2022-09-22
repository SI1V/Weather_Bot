from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

key_city = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Москва'),
            KeyboardButton('Пушкино'),
            KeyboardButton('Люберцы'),
            KeyboardButton('Оренбург')
        ],
        [
            KeyboardButton('Санкт-Петербург'),
            KeyboardButton('Рязань'),
            KeyboardButton('Курск')
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)