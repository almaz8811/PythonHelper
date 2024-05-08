import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command
from config_data.config import Config, load_config

config: Config = load_config()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.tg_bot.token)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Hello!')


# Хэндлер на команду /test1
@dp.message(Command('test1'))
async def cmd_test1(message: Message):
    await message.reply('Test 1')


# Хэндлер на команду /test2
async def cmd_test2(message: Message):
    await message.reply('Test 2')


# Запуск процесса поллинга новых апдейтов
async def main():
    dp.message.register(cmd_test2, Command('test2'))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
