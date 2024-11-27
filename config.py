from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

Staff = [195673497, ]

token = config('TOKEN')
bot = BOT = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)