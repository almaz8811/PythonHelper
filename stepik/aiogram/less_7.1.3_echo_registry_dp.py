'''
##### 7.1.3 #####
Регистрация хэндлеров в диспетчере
'''

import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

token = os.getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду '/start'
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут эхо-бот!\nНапиши мне что-нибудь!')


# Этот хэндлер будет срабатывать на команду '/help'
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь в ответ и я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на любые ваши сообщения
# кроме команд '/start' и '/help'
async def send_echo(message: Message):
    await message.reply(text=message.text)


# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands=['start']))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
