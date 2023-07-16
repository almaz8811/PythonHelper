from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import CommandStart, Text
from config_data.config import Config, load_config

config: Config = load_config()

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()

# Создаем объекты инлайн-кнопок
big_button_1: InlineKeyboardButton = InlineKeyboardButton(text='БОЛЬШАЯ КНОПКА 1',
                                                          callback_data='big_button_1_pressed')
big_button_2: InlineKeyboardButton = InlineKeyboardButton(text='БОЛЬШАЯ КНОПКА 2',
                                                          callback_data='big_button_2_pressed')

# Создаем объект инлайн-клавиатуры
keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[big_button_1], [big_button_2]])


# Этот хэндлер будет срабатывать на команду /start и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Это инлайн-кнопки. Нажми на любую!', reply_markup=keyboard)


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed' или 'big_button_1_pressed'
# @dp.callback_query(Text(text=['big_button_1_pressed', 'big_button_2_pressed']))
# async def process_button_press(callback: CallbackQuery):
#     await callback.answer()


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@dp.callback_query(Text(text=['big_button_1_pressed']))
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        # Параметр reply_markup=callback.message.reply_markup говорит о том, что в качестве клавиатуры
        # к измененному сообщению мы прикрепляем ту же клавиатуру, которая пришла в хэндлер вместе с апдейтом.
        # То есть, мы будем менять только текст над кнопками, а сами кнопки оставлять такими же.
        await callback.message.edit_text(text='Была нажата БОЛЬШАЯ КНОПКА 1',
                                         reply_markup=callback.message.reply_markup)
    await callback.answer()


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_2_pressed'
@dp.callback_query(Text(text=['big_button_2_pressed']))
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(text='Была нажата БОЛЬШАЯ КНОПКА 2',
                                         reply_markup=callback.message.reply_markup)
    await callback.answer()


if __name__ == '__main__':
    # Запускаем поллинг
    dp.run_polling(bot)
