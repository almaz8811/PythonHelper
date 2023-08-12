"""
С версии aiogram 3.0.0b8:
@dp.message(Text(text='more'))          ->  @dp.message(F.text == 'more')
@dp.callback_query(Text(text='more'))   ->  @dp.callback_query(F.data == 'more')
@dp.callback_query(Text(text=['text', 'audio', 'video', 'document', 'photo', 'voice'])) ->
@dp.callback_query(F.data.in_({'text', 'audio', 'video', 'document', 'photo', 'voice'}))
"""
from aiogram import Bot, Dispatcher, F
from aiogram.types import (Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup,
                           InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart, Command
from aiogram.exceptions import TelegramBadRequest

from config_data.config import Config, load_config

config: Config = load_config()
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()

LEXICON: dict[str, str] = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo1': '🖼 Фото',
    'photo2': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим текстовым сообщением,'
              'но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение,'
              'которое можно заменить на другое текстовое сообщение через редактирование.',
    'photo_id1': 'AgACAgIAAxkBAAIEGmTP8ccEkIpFo_fYihJnOAABx4A9lQAC7dIxGwNYgUqX0PpHWp5NeAEAAwIAA3MAAzAE',
    'photo_id2': 'AgACAgIAAxkBAAIEHGTP8k_DJNaHgzeDkc3g0rwWnvZmAAIC0zEbA1iBSoiKhpOkTFRPAQADAgADcwADMAQ',
    'voice_id1': 'AwACAgIAAxkBAAIEKmTP9Vy75QRsMNhK1_aiuG-GmtQZAAK_NgACA1iBSjgy3oWkgHxIMAQ',
    'voice_id2': 'AwACAgIAAxkBAAIELGTP9XnMH0hDJpVmUvzlLvxb_lfhAALCNgACA1iBSh4LM7lM7RTVMAQ',
    'audio_id1': 'CQACAgIAAxkBAAIEHmTP9CzkZEKP2Dp0YyHHqRmyko6cAAKsNgACA1iBSkcj8d-aqv10MAQ',
    'audio_id2': 'CQACAgIAAxkBAAIEIGTP9FCqgHMnhAABignJluiQQz-xEQACrTYAAgNYgUp_Zx9XeTFMFTAE',
    'document_id1': 'BQACAgIAAxkBAAIEImTP9HWZ1Ppr_Edd2fkJHllOHo3oAAKwNgACA1iBSuxaWCLQ-0YLMAQ',
    'document_id2': 'BQACAgIAAxkBAAIEJGTP9JFW4wubsEoCpbwoPz7tcNxLAAKyNgACA1iBSnZSGPg_ENVJMAQ',
    'video_id1': 'BAACAgIAAxkBAAIEJmTP9M5DuAWFjoKkKEAgr76LcKLmAAK1NgACA1iBSmJVGlnyfNIpMAQ',
    'video_id2': 'BAACAgIAAxkBAAIEKGTP9SaN_9EG4yWDoPtCDgxETSY9AAK7NgACA1iBSuWGxtbqdKplMAQ'}


# Функция для генерации клавиатур с инлайн-кнопками
def get_markup(*args, **kwargs) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text, callback_data=button))
    # Распаковываем список с кнопками в билдер методом row с параметром width
    kb_builder.row(*buttons, width=1)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команды "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками
    buttons.append(InlineKeyboardButton(
        text=f'{LEXICON["text"]} > {LEXICON["text"]}',
        callback_data='text_to_text'))
    buttons.append(InlineKeyboardButton(
        text=f'{LEXICON["text"]} > {LEXICON["photo1"]}',
        callback_data='text_to_photo'))
    buttons.append(InlineKeyboardButton(
        text=f'{LEXICON["photo1"]} > {LEXICON["photo2"]}',
        callback_data='photo_to_photo'))
    buttons.append(InlineKeyboardButton(text=LEXICON['audio'], callback_data='start_audio'))
    buttons.append(InlineKeyboardButton(text=LEXICON['video'], callback_data='start_video'))
    buttons.append(InlineKeyboardButton(text=LEXICON['document'], callback_data='start_document'))
    buttons.append(InlineKeyboardButton(text=LEXICON['voice'], callback_data='start_voice'))
    # Распаковываем список с кнопками в билдер методом row с параметром width
    kb_builder.row(*buttons, width=1)
    # Возвращаем объект инлайн-клавиатуры
    await message.answer(text='Выберите тип сообщения', reply_markup=kb_builder.as_markup())


# Этот хэндлер будет срабатывать на команду "text_to_text"
@dp.callback_query(F.data == 'text_to_text')
async def process_text_to_text_command(callback: CallbackQuery):
    markup = get_markup('text')
    await callback.message.answer(text=LEXICON['text_1'], reply_markup=markup)


# Этот хэндлер будет срабатывать на команду "text_to_photo"
@dp.callback_query(F.data == 'text_to_photo')
async def process_text_to_photo_command(callback: CallbackQuery):
    markup = get_markup('photo1')
    await callback.message.answer(text=LEXICON['text_1'], reply_markup=markup)


# Этот хэндлер будет срабатывать на команду "photo_to_photo"
@dp.callback_query(F.data == 'photo_to_photo')
async def process_photo_to_photo_command(callback: CallbackQuery):
    markup = get_markup('photo2')
    await callback.message.answer_photo(photo=LEXICON['photo_id1'], caption='Это фото 1', reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@dp.callback_query(F.data.in_({'text', 'photo1', 'photo2', 'audio', 'video', 'document', 'voice'}))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    match callback.data:
        # Меняем текст на текст
        case 'text':
            markup = get_markup('text')
            if callback.message.text == LEXICON['text_1']:
                text = LEXICON['text_2']
            else:
                text = LEXICON['text_1']
            await callback.message.edit_text(text=text, reply_markup=markup)
        case 'photo1':
            # Меняем текст на медиа. Будет исключение:
            # aiogram.exceptions.TelegramBadRequest:
            # Telegram server says Bad Request: there is no media in the message to edit
            markup = get_markup('photo1')
            await bot.edit_message_media(
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                media=InputMediaPhoto(media=LEXICON['photo_id1'], caption='Это фото 1'),
                reply_markup=markup)
        case 'photo2':
            # Меняем фото на фото
            markup = get_markup('photo2')
            try:
                await bot.edit_message_media(
                    chat_id=callback.message.chat.id,
                    message_id=callback.message.message_id,
                    media=InputMediaPhoto(media=LEXICON['photo_id2'], caption='Это фото 2'),
                    reply_markup=markup)
            except TelegramBadRequest:
                await bot.edit_message_media(
                    chat_id=callback.message.chat.id,
                    message_id=callback.message.message_id,
                    media=InputMediaPhoto(media=LEXICON['photo_id1'], caption='Это фото 1'),
                    reply_markup=markup)


# Этот хэндлер будет срабатывать на любые сообщения, кроме команд,
# отлавливаемых хэндлерами выше
@dp.message()
async def send_echo(message: Message):
    print(message)
    await message.answer(text='Не понимаю')


if __name__ == '__main__':
    dp.run_polling(bot)
