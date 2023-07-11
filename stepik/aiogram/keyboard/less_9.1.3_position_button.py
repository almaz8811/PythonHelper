from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from config_data.config import Config, load_config

config: Config = load_config()

bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()

# Пример 1 - Создаем клавиатуру из 3-х рядов кнопок по 3 кнопки в каждом ряду
# Создаем объекты кнопок
# button_1: KeyboardButton = KeyboardButton(text='Кнопка 1')
# button_2: KeyboardButton = KeyboardButton(text='Кнопка 2')
# button_3: KeyboardButton = KeyboardButton(text='Кнопка 3')
# button_4: KeyboardButton = KeyboardButton(text='Кнопка 4')
# button_5: KeyboardButton = KeyboardButton(text='Кнопка 5')
# button_6: KeyboardButton = KeyboardButton(text='Кнопка 6')
# button_7: KeyboardButton = KeyboardButton(text='Кнопка 7')
# button_8: KeyboardButton = KeyboardButton(text='Кнопка 8')
# button_9: KeyboardButton = KeyboardButton(text='Кнопка 9')
# Создаем объект клавиатуры, добавляя в него кнопки
# my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2, button_3],
#                                                                  [button_4, button_5, button_6],
#                                                                  [button_7, button_8, button_9]],
#                                                        resize_keyboard=True)

# Пример 2 - Создаем клавиатуру из 3-х рядов кнопок по 3 кнопки в каждом ряду
# Создаем объекты кнопок
# keyboard: list[list[KeyboardButton]] = [[KeyboardButton(
#                                         text=f'Кнопка {j * 3 + i}') for i in range(1, 4)] for j in range(3)]
# Создаем объект клавиатуры, добавляя в него кнопки
# my_keyboard : ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

# Пример 3 - Клавиатура из 9 кнопок в 5 рядах
# Генерируем список с кнопками
# buttons: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i}') for i in range(1, 10)]
# Составляем список списков для будущей клавиатуры
# keyboard: list[list[KeyboardButton]] = [[buttons[0]],
#                                         buttons[1:3],
#                                         buttons[3:6],
#                                         buttons[6:8],
#                                         [buttons[8]]]
# Создаем объект клавиатуры, добавляя в него список списков с кнопками
# my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

# Пример 4 - 2 ряда кнопок по 30 кнопок в каждом ряду
# Генерируем список с кнопками
# buttons_1: list[KeyboardButton] = [KeyboardButton(text=f'{i}') for i in range(1, 31)]
# Генерируем список с кнопками
# buttons_2: list[KeyboardButton] = [KeyboardButton(text=f'{i}') for i in range(31, 61)]
# Составляем список списков для будущей клавиатуры
# keyboard: list[list[KeyboardButton]] = [buttons_1, buttons_2]
# Создаем объект клавиатуры, добавляя в него список списков с кнопками
# my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

# Пример 5 - 100 рядов по 12 кнопок в каждом
# buttons: list[KeyboardButton] = []
# keyboard: list[list[KeyboardButton]] = []
# Заполняем список списками с кнопками
# for i in range(1, 1201):
#     buttons.append(KeyboardButton(text=str(i)))
#     if not i % 12:
#         keyboard.append(buttons)
#         buttons = []
# Создаем объект клавиатуры, добавляя в него список списков с кнопками
# my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

# Пример 6 - 350 рядов кнопок по одной кнопке в каждом ряду
# Заполняем список списками с кнопками
keyboard: list[list[KeyboardButton]] = [[KeyboardButton(text=f'Кнопка {i}')] for i in range(1, 351)]
# Создаем объект клавиатуры, добавляя в него список списков с кнопками
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду /start
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура', reply_markup=my_keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)
