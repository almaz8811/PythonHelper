import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters.command import Command, CommandObject
from aiogram.utils.media_group import MediaGroupBuilder
from config_data.config import Config, load_config

config: Config = load_config()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.tg_bot.token)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Hello!')


# Хэндлер на команду с аргументами /args
@dp.message(Command('args'))
async def cmd_args(message: Message, command: CommandObject):
    # Если не переданы никакие аргументы, то command.args будет None
    if command.args is None:
        await message.answer('Ошибка: не переданы аргументы')
        return
    # Пробуем разделить аргументы на две части по первому встречному пробелу
    try:
        delay_time, text_to_send = command.args.split(' ', maxsplit=1)
    # Если получилось меньше двух частей, вылетит ValueError
    except ValueError:
        await message.answer('Ошибка: неправильный формат команды. Пример:\n'
                             '/args <time> <message>')
        return
    await message.answer('Таймер добавлен!\n'
                         f'Время: {delay_time}\n'
                         f'Текст: {text_to_send}')


# Заставим бота реагировать на команды с другими префиксами
@dp.message(Command('custom1', prefix='%'))
async def cmd_custom1(message: Message):
    await message.answer('Вижу команду!')


# То же самое, с несколькими префиксами
@dp.message(Command('custom2', prefix='/!'))
async def cmd_custom2(message: Message):
    await message.answer('И это тоже команда!')


# Хэндлер отправляет пользователю в ответ эту же гифку, используя file_id
@dp.message(F.animation)
async def echo_gif(message: Message):
    await message.reply_animation(message.animation.file_id)


# Пример отправки изображений тремя способами FSInputFile, BufferedInputFile, URLInputFile
@dp.message(Command('images'))
async def upload_photo(message: Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []

    # Чтобы продемонстрировать BufferedInputFile, воспользуемся 'классическим' открытием файла
    # через 'open()'. Но, вообще говоря, этот способ лучше всего подходит для отправки байтов
    # из оперативной памяти после проведения каких-либо манипуляций, например, редактированием через Pillow
    with open('buffer_emulation.jpg', 'rb') as image_from_buffer:
        result = await message.answer_photo(BufferedInputFile(image_from_buffer.read(),
                                                              filename='image from buffer.jpg'),
                                            caption='Изображение из буфера')
        file_ids.append(result.photo[-1].file_id)

    # Отправка файли из файловой системы
    image_from_pc = FSInputFile('image_from_pc.jpg')
    result = await message.answer_photo(image_from_pc, caption='Изображение из файла на компьютере')
    file_ids.append(result.photo[-1].file_id)

    # Отправка файла по ссылке
    image_from_url = URLInputFile('https://picsum.photos/seed/groosha/400/300')
    result = await message.answer_photo(image_from_url, caption='Изображение по ссылке')
    file_ids.append(result.photo[-1].file_id)
    await message.answer('Отправленные файлы:\n' + '\n'.join(file_ids))


# Скачивание файлов
@dp.message(F.photo)
async def download_photo(message: Message, bot: Bot):
    await bot.download(message.photo[-1],
                       destination=f'/tmp/{message.photo[-1].file_id}.jpg')


@dp.message(F.sticker)
async def download_sticker(message: Message, bot: Bot):
    await bot.download(message.sticker,
                       destination=f'/tmp/{message.sticker.file_id}.webp')


# Отправка альбома с медиа файлами
@dp.message(Command('album'))
async def cmd_album(message: Message):
    album_builder = MediaGroupBuilder(caption='Общая подпись для будущего альбома')
    album_builder.add(type='photo',
                      media=FSInputFile('image_from_pc.jpg'))
    # Если мы сразу знаем тип, то вместо общего add можно сразу вызвать add_<тип>
    # Для ссылок или file_id достаточно сразу указать значение
    album_builder.add_photo(media='https://picsum.photos/seed/groosha/400/300')
    album_builder.add_photo(media='<file_id>')
    await message.answer_media_group(media=album_builder.build())

if __name__ == '__main__':
    dp.run_polling(bot)
