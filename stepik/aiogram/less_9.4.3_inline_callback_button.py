"""
В рамках класса InlineKeyboardBuilder доступны основные методы:
- row() - для добавления в билдер списка кнопок.
  Параметр width отвечает за то, сколько кнопок будет в одном ряду, когда клавиатура будет отправлена пользователю
- add() - этим методом кнопки добавляются в последний ряд клавиатуры, если их там еще меньше 8.
  Если в последнем ряду уже и так 8 кнопок - кнопки добавляются в новый ряд.
  Метод add() игнорирует параметр width метода row(), если он вызывался ранее.
  То есть кнопки в ряду заполняются до 8, не зависимо от того, что указано в width метода row()
- adjust() - метод, позволяющий расположить кнопки, добавленные методом row(), в кастомной конфигурации.
  Метод игнорирует параметр width метода row()
- copy() - метод, позволяющий получить полную копию билдера.
  Например, если вы хотите создать похожую клавиатуру, модифицировав старую, но не меняя саму старую клавиатуру
- export() - метод, позволяющий получить список списков с кнопками из билдера
- as_markup() - метод, превращающий билдер в объект инлайн-клавиатуры InlineKeyboardMarkup
"""

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
big_button_3: InlineKeyboardButton = InlineKeyboardButton(text='БОЛЬШАЯ КНОПКА 3',
                                                          callback_data='big_button_3_pressed')

# Создаем объект инлайн-клавиатуры
keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[big_button_1], [big_button_2], [big_button_3]])


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
    # Отправляем пустой ответ, чтобы callback понял, что команда обработана
    await callback.answer()


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_2_pressed'
@dp.callback_query(Text(text=['big_button_2_pressed']))
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(text='Была нажата БОЛЬШАЯ КНОПКА 2',
                                         reply_markup=callback.message.reply_markup)
    # Или создаем всплывающее окно с нотификацией
    await callback.answer('Ура! Нажата кнопка 2')


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_3_pressed'
@dp.callback_query(Text(text=['big_button_3_pressed']))
async def process_button_3_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 3':
        await callback.message.edit_text(text='Была нажата БОЛЬШАЯ КНОПКА 3',
                                         reply_markup=callback.message.reply_markup)
    # Или создаем всплывающее окно alert, которое требует нажатия от пользователя
    await callback.answer('Ура! Нажата кнопка 3', show_alert=True)


if __name__ == '__main__':
    # Запускаем поллинг
    dp.run_polling(bot)
