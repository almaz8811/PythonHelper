import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config_data.config import Config, load_config

config: Config = load_config()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.tg_bot.token)
# Диспетчер
dp = Dispatcher()


# Хэндлер, который отправляет сообщение с двумя кнопками на команду /start
@dp.message(Command('start'))
async def cmd_start(message: Message):
    kb = [[KeyboardButton(text='С пюрешкой'), KeyboardButton(text='Без пюрешки')]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                   input_field_placeholder='Выберите способ подачи')
    await message.answer('Как подавать котлеты?', reply_markup=keyboard)


@dp.message(F.text.lower() == 'с пюрешкой')
async def with_puree(message: Message):
    await message.answer('Отличный выбор!')


@dp.message(F.text.lower() == 'без пюрешки')
async def without_puree(message: Message):
    await message.answer('Так не вкусно!')


# Сборщик клавиатур

@dp.message(Command('reply_builder'))
async def reply_builder(message: Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 17):
        builder.add(KeyboardButton(text=str(i)))
    builder.adjust(4)
    await message.answer('Выберите число:', reply_markup=builder.as_markup(resize_keyboard=True))


if __name__ == '__main__':
    dp.run_polling(bot)
