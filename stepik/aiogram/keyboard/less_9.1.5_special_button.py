from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, Message
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config_data.config import Config, load_config

config: Config = load_config()

bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()

# Инициализируем билдер
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Создаем кнопки
contact_btn: KeyboardButton = KeyboardButton(text='Отправить телефон', request_contact=True)
geo_btn: KeyboardButton = KeyboardButton(text='Отправить геолокацию', request_location=True)
poll_btn: KeyboardButton = KeyboardButton(text='Создать опрос/викторину', request_poll=KeyboardButtonPollType())
# Добавляем кнопки в билдер
kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)
# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


# Этот хэндлер будет срабатывать на команду /start
# и отправлять в чат клавиатуру
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer(text='Экспериментируем со специальными кнопками', reply_markup=keyboard)


# Можно конкретизировать, что именно (опрос или викторина) будет создаваться по кнопке,
# если в KeyboardButtonPollType передать соответствующий тип:
# type='quiz' - викторина
# type='regular' - опрос

# Создаем кнопки
poll_btn_2: KeyboardButton = KeyboardButton(text='Создать опрос', request_poll=KeyboardButtonPollType(type='regular'))
quiz_btn: KeyboardButton = KeyboardButton(text='Создать викторину', request_poll=KeyboardButtonPollType(type='quiz'))
# Инициализируем билдер
poll_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Добавляем кнопки в билдер
poll_kb_builder.row(poll_btn_2, quiz_btn, width=1)
# Создаем объект клавиатуры
poll_keyboard: ReplyKeyboardMarkup = poll_kb_builder.as_markup(resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду /poll
# и отправлять в чат клавиатуру
@dp.message(Command(commands=['poll']))
async def process_poll_command(message: Message):
    await message.answer(text='Экспериментируем с кнопками опрос/викторина', reply_markup=poll_keyboard)


# WebApp-кнопка
# Создаем кнопку
web_app_btn: KeyboardButton = KeyboardButton(text='Start Web App', web_app=WebAppInfo(url='https://stepik.org/'))
# Создаем объект клавиатуры
web_app_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[web_app_btn]], resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду /web_app
# и отправлять в чат клавиатуру
@dp.message(Command(commands=['web_app']))
async def process_web_app_command(message: Message):
    await message.answer(text='Экспериментируем с кнопками опрос/викторина', reply_markup=web_app_keyboard)


'''
Дополнительные параметры кнопок
input_field_placeholder у объекта клавиатуры ReplyKeyboardMarkup - отвечает за подсказку в поле ввода

Отвечает за то, чтобы клавиатура появлялась и удалялась не у всех пользователей, а только у некоторых
selective у объекта клавиатуры ReplyKeyboardMarkup
selective у объекта удаления клавиатуры ReplyKeyboardRemove
'''
# Создаем кнопки
btn_1: KeyboardButton = KeyboardButton(text='Кнопка 1')
btn_2: KeyboardButton = KeyboardButton(text='Кнопка 2')
# Создаем объект клавиатуры
placeholder_example_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[btn_1, btn_2]],
                                                                  resize_keyboard=True,
                                                                  input_field_placeholder='Нажмите кнопку 1')


# Этот хэндлер будет срабатывать на команду /placeholder
# и отправлять в чат клавиатуру
@dp.message(Command(commands=['placeholder']))
async def process_placeholder_command(message: Message):
    await message.answer(text='Экспериментируем с полем placeholder', reply_markup=placeholder_example_kb)


if __name__ == '__main__':
    dp.run_polling(bot)
