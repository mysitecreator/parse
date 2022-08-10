from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
import config

from main import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

btnRandom = KeyboardButton('Рандомный продукт')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user),
                           reply_markup=mainMenu)

    print(message.from_user)

@dp.message_handler()
async def bot_message(message: types.Message):
    test = await get_random_product()

    keyboard = types.InlineKeyboardMarkup()

    if message.text == 'Рандомный продукт':
        await bot.send_photo(message.from_user.id, types.InputFile.from_url(test['image']),
                             f"Продукт: {test['title']}\n \nЦена: {test['price']}"
                             f"\n\nКупить: {test['link']}", reply_markup=keyboard)

    print(message.from_user, message.chat, message.text)
    print(message.text)

executor.start_polling(dp, skip_updates=True)
