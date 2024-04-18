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
dp: Dispatcher = Dispatcher(storage=storage)

# Создаем "базу данных" пользователей
user_dict: dict[int, dict[str, str | int | bool]] = {}


# Создаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSMFillForm(StatesGroup):
    # Создаем экземпляры класса State, последовательно перечисляя возможные состояния,
    # в которых будет находиться бот в разные моменты взаимодействия с пользователем
    fill_name: State = State()  # Состояние ожидания ввода имени
    fill_age: State = State()  # Состояние ожидания ввода возраста
    fill_gender: State = State()  # Состояние ожидания ввода пола
    upload_photo: State = State()  # Состояние ожидания загрузки фото
    fill_education: State = State()  # Состояние ожидания выбора образования
    fill_wish_news: State = State()  # Состояние ожидания выбора получать ли новости


# Этот хэндлер будет срабатывать на команду /start вне состояний
# и предлагать перейти к заполнению анкеты, отправив команду /fillform
@dp.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(text='Этот бот демонстрирует работу FSM\n\n'
                              'Чтобы перейти к заполнению анкеты - '
                              'отправьте команду /fillform')


# Этот хэндлер будет срабатывать на команду /cancel в состоянии
# по умолчанию и сообщать, то эта команда работает внутри машины состояний
@dp.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer('Отменять нечего. Вы вне машины состояний\n\n'
                         'Чтобы перейти к заполнению анкеты - '
                         'отправьте команду /fillform')

# Этот хэндлер будет срабатывать на команду /cancel в любых состояниях,
# кроме состояния по умолчанию, и отключать машину состояний
@dp.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer('Вы вышли из машины состояний\n\n'
                         'Чтобы снова перейти к заполнению анкеты - '
                         'отправьте команду /fillform')
    # Сбрасывает состояние и очищаем данные, полученные внутри состояний
    await state.clear()

# Этот хэндлер будет срабатывать на команду /fillform и переводить бота в состояние ожидания ввода имени
@dp.message(Command(commands='fillform'), StateFilter(default_state))
async def process_fillform_command(message: Message, state: FSMContext):
    await message.answer(text='Пожалуйста, ведите ваше имя')
    # Устанавливаем состояние ожидания ввода имени
    await state.set_state(FSMFillForm.fill_name)