import logging
import re
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters.command import Command, CommandObject, CommandStart
from config_data.config import Config, load_config

config: Config = load_config()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.tg_bot.token)
# Диспетчер
dp = Dispatcher()


@dp.message(Command('help'))
@dp.message(CommandStart(deep_link=True, magic=F.args == 'help'))
async def cmd_start_help(message: Message):
    await message.answer('Это сообщение со справкой')


@dp.message(CommandStart(deep_link=True, magic=F.args.regex(re.compile(r'book_(\d+)'))))
async def cmd_start_book(message: Message, command: CommandObject):
    book_number = command.args.split('_')[1]
    await message.answer(f'Sending book №{book_number}')


if __name__ == '__main__':
    dp.run_polling(bot)
