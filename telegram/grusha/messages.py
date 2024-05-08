import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command, CommandObject
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


# Хэндлер на команду с аргументами /args
@dp.message(Command('args'))
async def cmd_args(message: Message, command: CommandObject):
    # Если не переданы никакие аргументы, то command.args будет None
    if command.args is None:
        await message.answer('Ошибка: не переданы аргументы')
        return
    # Пробуем разделить аргументы на две части по первому встречному пробелу
    try:
        delay_time, text_to_send = command.args.split(' ', maxsplit=1)
    # Если получилось меньше двух частей, вылетит ValueError
    except ValueError:
        await message.answer('Ошибка: неправильный формат команды. Пример:\n'
                             '/args <time> <message>')
        return
    await message.answer('Таймер добавлен!\n'
                         f'Время: {delay_time}\n'
                         f'Текст: {text_to_send}')


if __name__ == '__main__':
    dp.run_polling(bot)
