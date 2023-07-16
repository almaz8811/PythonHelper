from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from config_data.config import Config, load_config

config: Config = load_config()

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()

# Создаем объекты инлайн-кнопок
url_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Курс "Телеграм-боты на Python и Aiogram"',
    url='https://stepik.org/120924')
url_button_2: InlineKeyboardButton = InlineKeyboardButton(text='Документация Telegram Bot API',
                                                          url='https://core.telegram.org/bots/api')
group_name = 'aiogram_stepik_course'
url_button_3: InlineKeyboardButton = InlineKeyboardButton(text='Группа "Телеграм-боты на Aiogram"',
                                                          url=f'tg://resolve?domain={group_name}')
user_id = config.tg_bot.user_id
url_button_4: InlineKeyboardButton = InlineKeyboardButton(text='Автор курса на Степике по телеграм-ботам',
                                                          url=f'tg://user?id={user_id}')
channel_name = 'toBeAnMLspecialist'
url_button_5: InlineKeyboardButton = InlineKeyboardButton(text='Канал "Стать специалистом по машинному обучению"',
                                                          url=f'https://t.me/{channel_name}')

# Создаем объект инлайн-клавиатуры
keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[url_button_1],
                                                                       [url_button_2],
                                                                       [url_button_3],
                                                                       [url_button_4],
                                                                       [url_button_5]])


# Этот хэндлер будет срабатывать на команду /start и отправлять в чат клавиатуру с url-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Это инлайн-кнопки с параметром "url"', reply_markup=keyboard)


if __name__ == '__main__':
    # Запускаем поллинг
    dp.run_polling(bot)
