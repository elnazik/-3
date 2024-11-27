from aiogram import types, Dispatcher
from config import bot, dp


async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}\n'
                                f'Твой Telegram id: {message.from_user.id}\n')
    await message.answer('Hello')



def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')