import logging
from random import randint
from contextlib import suppress
from typing import Optional
from aiogram import Bot, Dispatcher, F
from aiogram import flags
from aiogram.filters.command import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.callback_answer import CallbackAnswerMiddleware, CallbackAnswer
from config_data.config import Config, load_config

config: Config = load_config()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.tg_bot.token)
# Диспетчер
dp = Dispatcher()
# В этом случае после выполнения хэндлера aiogram будет автоматически отвечать на колбэк
# dp.callback_query.middleware(CallbackAnswerMiddleware())
# Можно переопределить стандартные настройки и указать свои
dp.callback_query.middleware(CallbackAnswerMiddleware(pre=True, text='Готово', show_alert=True))


@dp.callback_query()
@flags.callback_answer(pre=False)
async def my_handler(callback: CallbackQuery, callback_answer: CallbackAnswer):
    # ... тут какой-то код
    if 1 != 2:
        callback_answer.text = 'Отлично'
    else:
        callback_answer.text = 'Что-то пошло не так. Попробуйте позже'
        callback_answer.cache_time = 10


if __name__ == '__main__':
    dp.run_polling(bot)
