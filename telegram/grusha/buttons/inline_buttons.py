import logging
from random import randint
from contextlib import suppress
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest

from typing import Optional
from config_data.config import Config, load_config

config: Config = load_config()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.tg_bot.token)
# Диспетчер
dp = Dispatcher()


@dp.message(Command('inline_url'))
async def cmd_inline_url(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='GitHub', url='https://github.com'))
    builder.row(InlineKeyboardButton(text='Оф. канал Telegram', url='tg://resolve?domain=telegram'))
    # Чтобы иметь возможность показать ID-кнопку, у юзера должен быть False флаг has_private_forwards
    user_id = 1234567890
    chat_info = await bot.get_chat(user_id)
    if not chat_info.has_private_forwards:
        builder.row(InlineKeyboardButton(text='Какой-то пользователь', url=f'tg://user?id={user_id}'))
    await message.answer(text='Выберите ссылку', reply_markup=builder.as_markup())


# Колбэки

@dp.message(Command('random'))
async def cmd_random(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Нажми меня', callback_data='random_value'))
    await message.answer(text='Нажмите на кнопку, чтобы бот отправил число от 1 до 10',
                         reply_markup=builder.as_markup())


@dp.callback_query(F.data == 'random_value')
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer(text=str(randint(1, 10)))
    await callback.answer(text='Спасибо, что воспользовались ботом!', show_alert=True)
    # или просто await callback.answer()


# Здесь хранятся пользовательские данные
# Так как это словарь в памяти, то при перезапуске он очистится
user_data = {}


def get_keyboard():
    buttons = [[InlineKeyboardButton(text='-1', callback_data='num_decr'),
                InlineKeyboardButton(text='+1', callback_data='num_incr')],
               [InlineKeyboardButton(text='Подтвердить', callback_data='num_finish')]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def update_num_text(message: Message, new_value: int):
    with suppress(TelegramBadRequest):
        await message.edit_text(f'Укажите число: {new_value}', reply_markup=get_keyboard())


@dp.message(Command('numbers'))
async def cmd_numbers(message: Message):
    user_data[message.from_user.id] = 0
    await message.answer(text='Укажите число: 0', reply_markup=get_keyboard())


@dp.callback_query(F.data.startswith('num_'))
async def callbacks_num(callback: CallbackQuery):
    user_value = user_data.get(callback.from_user.id, 0)
    action = callback.data.split('_')[1]
    if action == 'incr':
        user_data[callback.from_user.id] = user_value + 1
        await update_num_text(callback.message, user_value + 1)
    elif action == 'decr':
        user_data[callback.from_user.id] = user_value - 1
        await update_num_text(callback.message, user_value - 1)
    elif action == 'finish':
        await callback.message.edit_text(text=f'Итого: {user_value}')
    await callback.answer()


# Фабрика колбэков

class NumbersCallbackFactory(CallbackData, prefix="fabnum"):
    action: str
    value: Optional[int] = None


def get_keyboard_fab():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="-2", callback_data=NumbersCallbackFactory(action="change", value=-2)
    )
    builder.button(
        text="-1", callback_data=NumbersCallbackFactory(action="change", value=-1)
    )
    builder.button(
        text="+1", callback_data=NumbersCallbackFactory(action="change", value=1)
    )
    builder.button(
        text="+2", callback_data=NumbersCallbackFactory(action="change", value=2)
    )
    builder.button(
        text="Подтвердить", callback_data=NumbersCallbackFactory(action="finish")
    )
    # Выравниваем кнопки по 4 в ряд, чтобы получилось 4 + 1
    builder.adjust(4)
    return builder.as_markup()


async def update_num_text_fab(message: Message, new_value: int):
    with suppress(TelegramBadRequest):
        await message.edit_text(
            f"Укажите число: {new_value}",
            reply_markup=get_keyboard_fab()
        )


@dp.message(Command("numbers_fab"))
async def cmd_numbers_fab(message: Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard_fab())


# Нажатие на одну из кнопок: -2, -1, +1, +2
@dp.callback_query(NumbersCallbackFactory.filter(F.action == "change"))
async def callbacks_num_change_fab(
        callback: CallbackQuery,
        callback_data: NumbersCallbackFactory
):
    # Текущее значение
    user_value = user_data.get(callback.from_user.id, 0)
    user_data[callback.from_user.id] = user_value + callback_data.value
    await update_num_text_fab(callback.message, user_value + callback_data.value)
    await callback.answer()


# Нажатие на кнопку "подтвердить"
@dp.callback_query(NumbersCallbackFactory.filter(F.action == "finish"))
async def callbacks_num_finish_fab(callback: CallbackQuery):
    # Текущее значение
    user_value = user_data.get(callback.from_user.id, 0)
    await callback.message.edit_text(f"Итого: {user_value}")
    await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)
