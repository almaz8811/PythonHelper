from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message, PhotoSize

from config_data.config import Config, load_config

config: Config = load_config()

# Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
storage: MemoryStorage = MemoryStorage()

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=config.tg_bot.token)

# Создаем "базу данных" пользователей
user_dict: dict[int, dict[str, str | int | bool]] = {}


# Создаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSMFillForm(StatesGroup):
    # Создаем экземпляры класса State, последовательно перечисляя возможные состояния,
    # в которых будет находиться бот в разные моменты взаимодействия с пользователем
    fill_name = State()  # Состояние ожидания ввода имени
    fill_age = State()  # Состояние ожидания ввода возраста
    fill_gender = State()  # Состояние ожидания ввода пола
    upload_photo = State()  # Состояние ожидания загрузки фото
    fill_education = State()  # Состояние ожидания выбора образования
    fill_wish_news = State()  # Состояние ожидания выбора получать ли новости
