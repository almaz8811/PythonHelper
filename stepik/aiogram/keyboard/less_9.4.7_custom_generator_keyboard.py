from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import CommandStart, Text
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config_data.config import Config, load_config

config: Config = load_config()

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()

LEXICON: dict[str, str] = {
    'but_1': 'Кнопка 1',
    'but_2': 'Кнопка 2',
    'but_3': 'Кнопка 3',
    'but_4': 'Кнопка 4',
    'but_5': 'Кнопка 5',
    'but_6': 'Кнопка 6',
    'but_7': 'Кнопка 7'
}
BUTTONS: dict[str, str] = {
    'btn_1': '1',
    'btn_2': '2',
    'btn_3': '3',
    'btn_4': '4',
    'btn_5': '5',
    'btn_6': '6',
    'btn_7': '7'
}


# Функция для генерации инлайн-клавиатур "на лету"
def create_inline_kb(width: int, *args: str, last_btn: str | None = None, **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kd_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(text=LEXICON[button] if button in LEXICON else button,
                                                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text, callback_data=button))
    # Распаковываем список с кнопками в билдер методом row с параметром width
    kd_builder.row(*buttons, width=width)
    # Добавляем в билдер последнюю кнопку, если она передана в функцию
    if last_btn:
        kd_builder.row(InlineKeyboardButton(text=last_btn, callback_data='last_btn'))
    # Возвращаем объект инлайн-клавиатуры
    return kd_builder.as_markup()


# Этот хэндлер будет срабатывать на команду /start и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    # Передать весь словарь BUTTONS с кнопками
    # keyboard = create_inline_kb(4, last_btn='Последняя кнопка', **BUTTONS)
    keyboard = create_inline_kb(2, 'but_1', 'but_3', 'but_7', 'but_9', last_btn='Последняя кнопка',
                                btn_tel='Телефон', btn_email='email', btn_website='Web-сайт',
                                btn_vk='VK', btn_tgbot='Наш телеграм-бот')
    await message.answer(text='Вот такая получается клавиатура', reply_markup=keyboard)


if __name__ == '__main__':
    # Запускаем поллинг
    dp.run_polling(bot)
