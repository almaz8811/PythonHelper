'''
##### 7.1.1 #####
Эхо-бот
'''

import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

token = os.getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду '/start'
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут эхо-бот!\nНапиши мне что-нибудь!')


# Этот хэндлер будет срабатывать на команду '/help'
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь в ответ и я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на любые ваши сообщения
# кроме команд '/start' и '/help'
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
