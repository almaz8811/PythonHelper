from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import KeyboardButton, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config_data.config import Config, load_config

config: Config = load_config()

bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()
text: str = 'Вот такая получается клавиатура'

'''
Метод row()
Метод row у класса ReplyKeyboardBuilder позволяет расположить кнопки клавиатуры автоматически, в зависимости от
параметра width - желаемого количества кнопок в ряду. "Лишние" кнопки переносятся на следующий ряд.
Не смотря на то, что Телеграм, как мы выяснили на предыдущем шаге, позволяет в одном ряду разместить до 12 кнопок, 
"строитель клавиатур" позволит разместить не больше 8. Попытка указать width больше 8 приведет к ошибке.
'''

# Пример 1 - Автоматическое размещение 10 кнопок с параметром width=4
# Инициализируем билдер
kb_builder_1: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Создаем список с кнопками
buttons_1: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 1}') for i in range(10)]
# Распаковываем список кнопок в билдер, указываем, что в одном ряду должно быть 4 кнопки
kb_builder_1.row(*buttons_1, width=4)


# Этот хэндлер будет срабатывать на команду /key1
# и отправлять в чат клавиатуру
@dp.message(Command(commands=['key1']))
async def process_key1_command(message: Message):
    await message.answer(text=text,
                         reply_markup=kb_builder_1.as_markup(resize_keyboard=True))


# Пример 2 - Автоматическое размещение 8 кнопок с параметром width=3
# Инициализируем билдер
kb_builder_2: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Создаем список с кнопками
buttons_2: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 1}') for i in range(8)]
# Распаковываем список кнопок в билдер, указываем, что в одном ряду должно быть 4 кнопки
kb_builder_2.row(*buttons_2, width=3)


# Этот хэндлер будет срабатывать на команду /key2
# и отправлять в чат клавиатуру
@dp.message(Command(commands=['key2']))
async def process_key2_command(message: Message):
    await message.answer(text=text,
                         reply_markup=kb_builder_2.as_markup(resize_keyboard=True))


# Пример 3 - Автоматическое размещение сначала 6-ти кнопок с параметром width=4,
# а затем еще 4-х кнопок с параметром width=3
# Инициализируем билдер
kb_builder_3: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Создаем первый список с кнопками
buttons_3: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 1}') for i in range(6)]
# Создаем второй список с кнопками
buttons_4: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 7}') for i in range(4)]
# Распаковываем список кнопок в билдер, указываем, что в одном ряду должно быть 4 кнопки
kb_builder_3.row(*buttons_3, width=4)
# Еще раз распаковываем список кнопок в билдер, указываем, что теперь в одном ряду должно быть 3 кнопки
kb_builder_3.row(*buttons_4, width=3)


# Этот хэндлер будет срабатывать на команду /key3
# и отправлять в чат клавиатуру
@dp.message(Command(commands=['key3']))
async def process_key3_command(message: Message):
    await message.answer(text=text,
                         reply_markup=kb_builder_3.as_markup(resize_keyboard=True))


'''
Метод add()
В отличие от метода row() метод add() добавляет кнопки с нового ряда только если в предыдущем ряду для новых кнопок 
уже нет места. Причем, методу add все равно какой там у вас был параметр width до этого. Кнопки будут добавляться 
в ряд пока их там не станет 8 и только потом начнут заполнять новый ряд. Тоже до 8 штук.
'''

# Пример 4 - Создадим клавиатуру, в которую добавим 5 кнопок методом row с параметром width=4,
# а затем добавим еще 10 кнопок методом add.
# Инициализируем билдер
kb_builder_4: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Создаем первый список с кнопками
buttons_5: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 1}') for i in range(5)]
# Создаем второй список с кнопками
buttons_6: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 6}') for i in range(10)]
# Распаковываем список кнопок в билдер, указываем, что в одном ряду должно быть 4 кнопки
kb_builder_4.row(*buttons_5, width=4)
# Еще раз распаковываем список кнопок в билдер
kb_builder_4.add(*buttons_6)


# Этот хэндлер будет срабатывать на команду /key4
# и отправлять в чат клавиатуру
@dp.message(Command(commands=['key4']))
async def process_key4_command(message: Message):
    await message.answer(text=text,
                         reply_markup=kb_builder_4.as_markup(resize_keyboard=True))


'''
Метод adjust()
Чтобы указать какое количество кнопок должно быть в каждом ряду - нужно передать в метод adjust 
целые числа (от 1 до 8), начиная с первого ряда. Причем данный метод будет игнорировать параметр width, 
если кнопки были добавлены в билдер методом row.
Можно указывать количество кнопок не для всех рядов. Тогда последующие ряды будут заполняться кнопками 
по значению последнего переданного аргумента. То есть, если у нас 7 кнопок, а мы в adjust добавили 2 и 1, 
то в первом ряду будет 2 кнопки, а во втором и последующих по одной.
'''

# Пример 5 - Создадим клавиатуру, добавив 8 кнопок методом add и расставим их так, чтобы в 1-м ряду была одна кнопка,
# во втором - 3, а остальные расставились бы автоматически.
# Инициализируем билдер
kb_builder_5: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Создаем первый список с кнопками
buttons_7: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 1}') for i in range(8)]
# Распаковываем список кнопок в билдер, методом add()
kb_builder_5.add(*buttons_7)
# Явно сообщаем билдеру, сколько хотим видеть кнопок в 1-м 2-м рядах
kb_builder_5.adjust(1, 3)


# Этот хэндлер будет срабатывать на команду /key5
# и отправлять в чат клавиатуру
@dp.message(Command(commands=['key5']))
async def process_key5_command(message: Message):
    await message.answer(text=text,
                         reply_markup=kb_builder_5.as_markup(resize_keyboard=True))


'''
Также у метода adjust есть параметр repeat, который по умолчанию равен False. Если сделать его True, 
то значения количества кнопок по рядам будут повторяться для новых рядов с кнопками.
'''
# Пример 6 - Создадим клавиатуру с 10 кнопками, переданными в билдер методом add и методом adjust
# разместим их по две в каждом нечетном ряду и по 1 в каждом четном.
# Инициализируем билдер
kb_builder_6: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Создаем первый список с кнопками
buttons_8: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 1}') for i in range(10)]
# Распаковываем список кнопок в билдер, методом add()
kb_builder_6.add(*buttons_8)
# Явно сообщаем билдеру, сколько хотим видеть кнопок в 1-м 2-м рядах,
# а также говорим методу повторять такое размещение для остальных рядов
kb_builder_6.adjust(2, 1, repeat=True)


# Этот хэндлер будет срабатывать на команду /key5
# и отправлять в чат клавиатуру
@dp.message(Command(commands=['key6']))
async def process_key6_command(message: Message):
    await message.answer(text=text,
                         reply_markup=kb_builder_6.as_markup(resize_keyboard=True))


if __name__ == '__main__':
    dp.run_polling(bot)
