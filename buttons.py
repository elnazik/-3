from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


a = True
cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=a)
cancel_button = KeyboardButton('Отмена')
cancel.add(cancel_button)

submit= ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=a, row_width=2).add(KeyboardButton('Да'),KeyboardButton('Нет'))