from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from config_data.config import Config, load_config

config: Config = load_config()
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()


# Создаем свой класс фабрики коллбэков, указывая префикс,
# а также структуру callback_data
class GoodCallbackFactory(CallbackData, prefix='goods', sep=':'):
    category_id: int
    subcategory_id: int
    item_id: int


# Создаем объекты кнопок, с применением фабрики коллбэков
button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Категория 1',
    callback_data=GoodCallbackFactory(category_id=1, subcategory_id=0, item_id=0).pack())
button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Категория 2',
    callback_data=GoodCallbackFactory(category_id=2, subcategory_id=0, item_id=0).pack())
# Создаем объект клавиатуры, добавляя в список списки с кнопками
markup: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2]])


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять пользователю сообщение с клавиатурой
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая клавиатура', reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие любой
# инлайн-кнопки и распечатывать апдейт в терминал
# @dp.callback_query()
# async def process_any_inline_button_press(callback: CallbackQuery):
#     print(callback.json(indent=4, exclude_none=True))
#     await callback.answer()

# Этот хэндлер будет срабатывать на нажатие любой
# инлайн-кнопки и отправлять категорию в чат
# @dp.callback_query(GoodCallbackFactory.filter())
# async def process_category_press(callback: CallbackQuery, callback_data: GoodCallbackFactory):
#     await callback.message.answer(text=callback_data.pack())
#     await callback.answer()


# Если мы хотим поймать только нажатие на первую кнопку ("Категория 1"),
# то нам в очередной раз может помочь магический фильтр
# @dp.callback_query(GoodCallbackFactory.filter(F.category_id == 1))
# async def process_category_press(callback: CallbackQuery, callback_data: GoodCallbackFactory):
#     await callback.message.answer(text=callback_data.pack())
#     await callback.answer()

# Этот хэндлер будет срабатывать на нажатие любой инлайн-кнопки
# и отправлять в чат форматированный ответ с данными из callback_data
@dp.callback_query(GoodCallbackFactory.filter())
async def process_category_press(callback: CallbackQuery, callback_data: GoodCallbackFactory):
    await callback.message.answer(
        text=f'Категория товаров: {callback_data.category_id}\n'
             f'Подкатегория товаров: {callback_data.subcategory_id}\n'
             f'Товар: {callback_data.item_id}')
    await callback.answer()


my_callback_data_1 = GoodCallbackFactory(category_id=2, subcategory_id=0, item_id=0)
print(my_callback_data_1.pack())

if __name__ == '__main__':
    dp.run_polling(bot)
