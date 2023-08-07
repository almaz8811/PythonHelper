"""
С версии aiogram 3.0.0b8:
@dp.message(Text(text='more'))          ->  @dp.message(F.text == 'more')
@dp.callback_query(Text(text='more'))   ->  @dp.callback_query(F.data == 'more')
@dp.callback_query(Text(text=['text', 'audio', 'video', 'document', 'photo', 'voice'])) ->
@dp.callback_query(F.data.in_({'text', 'audio', 'video', 'document', 'photo', 'voice'}))
"""
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.exceptions import TelegramBadRequest

from config_data.config import Config, load_config

config: Config = load_config()
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()

jokes: dict[int, str] = {
    1: 'с хабра, описание фильмов Матрица\n\n'
       'Судя по всему, в городе машин либо очень либеральный мэр, либо очень криворукие сисадмины.'
       'Иначе как объяснить, что свободные люди беспрепятственно подключаются к вражеской ИТ-системе?'
       'Причем удаленно из тарантаса, летающего по канализации! Т.е. мало того, что у машин в сточных трубах'
       'развернут высокоскоростной Wi-Fi, так они еще и пускают в свою сеть всех подряд, позволяя неавторизованным'
       'пользователям получать данные из системы, вносить в нее изменения и общаться между собой. Красота!',
    2: '- У меня на одном курсе был фин, он приехал к нам т.к. был очарован культурой гопников.'
       'Он хотел проникнуться ею у первоисточника и подтянуть мат. И вот где-то в Питере он припал к истокам,'
       'все-все выучил и загорелся желанием принести культуру другим иностранцам группы. А там были бразильцы,'
       'немцы итальянцы, французы и китаец. И вот захожу как-то я в группу и там хором повторяют слова "ъуъ" и "съка"'
       'с шестью разными акцентами.\n'
       '- Хотелось бы послушать, как они говорили "ъуъ"',
    3: 'Я в восторге от наших учителей.\n'
       'Сыну в школе дали домашнее задание, где, среди прочего, был вопрос "как связаны буква А4 и бык?"\n'
       'Рассказал ему про финикийский алфавит, как первую фонетическую письменность. Что там была буква "алеф",'
       'очень похожая на нашу современную "А", и что слово "алеф" означало "бык". Что, возможно, букву так назвали,'
       'потому что если развернуть ее, то она похожа на морду быка с рогами.\n'
       'Еще очень радовался, что детям во втором классе такие вещи рассказывают.\n'
       'Учительница поставила ребенку двойку, заявив, что он фантазировал в домашнем задании.'
       'А правильный ответ: если к слову "бык" добавить "а", получится родительный падеж.\n'
       'Я не планировал в таком раннем возрасте рассказывать сыну, что половина окружающих людей - идиоты,'
       'но, видимо, придется :-)',
    4: 'у меня на балконе сосулька растет метровая, прямо над машиной, которая ссигналит каждую ночь.'
       'Я эту сосульку из распылителя подкармливаю.',
    5: 'xx: Мне сейчас спам пришел "Я живу в доме напротив, вот моя ссылка *адрес ссылки*. Давай познакомимся".'
       'Я ответил, что живу напротив морга и меня пугают такие знакомства',
    6: 'xxx: В командировке на съемной квартире нужна была марля, чтобы погладить футболку.'
       'Начал шариться по всем ящикам. Марлю не нашел, зато нашел ключ в шкафу между простынями.'
       'Вспомнил, что один ящик в этом шкафу был заперт. Попробовал открыть его найденным ключом.'
       'Открыл. Внутри нашел марлю. Не зря в квесты играл..'}


# Функция, генерирующая случайное число в диапазоне от 1 до длины словаря jokes
def random_joke() -> int:
    return random.randint(1, len(jokes))


# Создаем клавиатуру
keyboard: list[list[InlineKeyboardButton]] = [
    [InlineKeyboardButton(text='Хочу еще! (без удаления)', callback_data='more_no_del')],
    [InlineKeyboardButton(text='Хочу еще! (с удалением)', callback_data='more_del')],
    [InlineKeyboardButton(text='Хочу еще! (с редактированием)', callback_data='more_edit')]]
markup: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=keyboard)


# Этот хэндлер будет срабатывать на команды "/start" и "/joke"
@dp.message(Command(commands=['start', 'joke']))
async def process_start_command(message: Message):
    await message.answer(text=jokes[random_joke()], reply_markup=markup)


# Отправка нового сообщения без удаления старого
@dp.callback_query(F.data == 'more_no_del')
async def process_more_no_del_press(callback: CallbackQuery):
    # Отвечаем на callback, чтобы убрать часики
    await callback.answer()
    # Отправляем в чат новое сообщение с шуткой
    await callback.message.answer(text=jokes[random_joke()], reply_markup=markup)


# Отправка нового сообщения с удалением старого
@dp.callback_query(F.data == 'more_del')
async def process_more_del_press(callback: CallbackQuery):
    # Удаляем сообщение, в котором была нажата кнопка
    await callback.message.delete()
    # Отправляем в чат новое сообщение с шуткой
    await callback.message.answer(text=jokes[random_joke()], reply_markup=markup)


# INFO: если в редактируемом сообщении ничего не меняется, то генерирует исключение вида
#  Telegram server says Bad Request: message is not modified: specified new message content and reply markup
#  are exactly the same as a current content and reply markup of the message

# Редактирование сообщения без проверки на совпадение
# @dp.callback_query(F.data == 'more_edit')
# async def process_more_edit_press(callback: CallbackQuery):
#     # редактируем текущее сообщение
#     await callback.message.edit_text(text=jokes[random_joke()], reply_markup=markup)

# Редактирование сообщения с проверкой на совпадение
@dp.callback_query(F.data == 'more_edit')
async def process_more_edit_press(callback: CallbackQuery):
    # Получаем текст шутки по ключу, сгенерированному функцией
    # random_joke и сохраняем в переменную text
    text = jokes[random_joke()]
    # Пока текст новой шутки совпадает со старым - генерируем новую шутку
    while text == callback.message.text:
        text = jokes[random_joke()]
    # Редактируем текущее сообщение гарантированно отличающимся текстом
    await callback.message.edit_text(text=text, reply_markup=markup)


# Редактирование сообщения с игнорированием исключения try\except
# @dp.callback_query(F.data == 'more_edit')
# async def process_more_edit_press(callback: CallbackQuery):
#     # Пытаемся отредактировать сообщение
#     try:
#         await callback.message.edit_text(text=jokes[random_joke()], reply_markup=markup)
#     except TelegramBadRequest:
#         # В случае возникновения исключения - игнорируем его, отвечая на коллбэк пустым ответом
#         await callback.answer()


# Этот хэндлер будет срабатывать на любые сообщения, кроме команд,
# отлавливаемых хэндлерами выше
@dp.message()
async def send_echo(message: Message):
    await message.answer(
        text='Я даже представить себе не могу, '
             'что ты имеешь в виду :(\n\n'
             'Чтобы получить какую-нибудь шутку - '
             'отправь команду /joke')


if __name__ == '__main__':
    dp.run_polling(bot)
