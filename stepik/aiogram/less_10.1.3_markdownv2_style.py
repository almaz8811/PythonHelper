from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config_data.config import Config, load_config

config: Config = load_config()
bot: Bot = Bot(token=config.tg_bot.token, parse_mode='MarkdownV2')
dp: Dispatcher = Dispatcher()


# Символы при работе в режиме MarkdownV2, которые не должны восприниматься телеграмом как часть разметки,
# должны быть экранированы символом '\'

# В случае, когда текст должен быть написан курсивом и подчеркнут одновременно,
# кажущееся логичным форматирование вида ___Наклонный подчеркнутый текст___ будет приводить к ошибке.
# Необходимо добавить специальный символ '\r' после первого подчеркивания в конце форматированного текста.
# То есть правильным вариантом будет ___Наклонный подчеркнутый текст_\r__.


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Привет\!\n\nЯ бот, демонстрирующий '
             'как работает разметка MardownV2\. Отправь команду '
             'из списка ниже:\n\n'
             '/bold \- жирный текст\n'
             '/italic \- наклонный текст\n'
             '/underline \- подчеркнутый текст\n'
             '/strike \- зачеркнутый текст\n'
             '/spoiler \- спойлер\n'
             '/link \- внешняя ссылка\n'
             '/tglink \- внутренняя ссылка\n'
             '/code \- моноширинный текст\n'
             '/pre \- предварительно форматированный текст\n'
             '/precode \- предварительно форматированный блок кода\n'
             '/boldi \- жирный наклонный текст\n'
             '/iu \- наклонный подчеркнутый текст\n'
             '/biu \- жирный наклонный подчеркнутый текст')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        text='Я бот, демонстрирующий '
             'как работает разметка MardownV2\. Отправь команду '
             'из списка ниже:\n\n'
             '/bold \- жирный текст\n'
             '/italic \- наклонный текст\n'
             '/underline \- подчеркнутый текст\n'
             '/strike \- зачеркнутый текст\n'
             '/spoiler \- спойлер\n'
             '/link \- внешняя ссылка\n'
             '/tglink \- внутренняя ссылка\n'
             '/code \- моноширинный текст\n'
             '/pre \- предварительно форматированный текст\n'
             '/precode \- предварительно форматированный блок кода\n'
             '/boldi \- жирный наклонный текст\n'
             '/iu \- наклонный подчеркнутый текст\n'
             '/biu \- жирный наклонный подчеркнутый текст')


# Этот хэндлер будет срабатывать на команду "/bold"
@dp.message(Command(commands='bold'))
async def process_bold_command(message: Message):
    await message.answer(
        text='\*Это жирный текст\*:\n'
             '*Это жирный текст*')


# Этот хэндлер будет срабатывать на команду "/italic"
@dp.message(Command(commands='italic'))
async def process_italic_command(message: Message):
    await message.answer(
        text='\_Это наклонный текст\_:\n'
             '_Это наклонный текст_')


# Этот хэндлер будет срабатывать на команду "/underline"
@dp.message(Command(commands='underline'))
async def process_underline_command(message: Message):
    await message.answer(
        text='\_\_Это подчеркнутый текст\_\_:\n'
             '__Это подчеркнутый текст__')


# Этот хэндлер будет срабатывать на команду "/strike"
@dp.message(Command(commands='strike'))
async def process_strike_command(message: Message):
    await message.answer(
        text='\~Это зачеркнутый текст\~:\n'
             '~Это зачеркнутый текст~')


# Этот хэндлер будет срабатывать на команду "/spoiler"
@dp.message(Command(commands='spoiler'))
async def process_spoiler_command(message: Message):
    await message.answer(
        text='\|\|Это текст под спойлером\|\|:\n'
             '||Это текст под спойлером||')


# Этот хэндлер будет срабатывать на команду "/link"
@dp.message(Command(commands='link'))
async def process_link_command(message: Message):
    await message.answer(
        text='\[Внешняя ссылка\]\(https://stepik\.org/120924\):\n'
             '[Внешняя ссылка](https://stepik.org/120924)')


# Этот хэндлер будет срабатывать на команду "/tglink"
@dp.message(Command(commands='tglink'))
async def process_tglink_command(message: Message):
    await message.answer(
        text=f'\[Внутренняя ссылка\]\(tg://user?id\={config.tg_bot.user_id}\):\n'
             f'[Внутренняя ссылка](tg://user?id={config.tg_bot.user_id})')


# Этот хэндлер будет срабатывать на команду "/code"
@dp.message(Command(commands='code'))
async def process_code_command(message: Message):
    await message.answer(
        text='\`Моноширинный текст\`:\n'
             '`Моноширинный текст`')


# Этот хэндлер будет срабатывать на команду "/pre"
@dp.message(Command(commands='pre'))
async def process_pre_command(message: Message):
    await message.answer(
        text='\`\`\` Предварительно отформатированный текст\`\`\`:\n'
             '``` Предварительно отформатированный текст```')


# Этот хэндлер будет срабатывать на команду "/precode"
@dp.message(Command(commands='precode'))
async def process_precode_command(message: Message):
    await message.answer(
        text='\`\`\`python Предварительно отформатированный блок '
             'кода на языке Python\`\`\`:\n'
             '```python Предварительно отформатированный блок '
             'кода на языке Python```')


# Этот хэндлер будет срабатывать на команду "/boldi"
@dp.message(Command(commands='boldi'))
async def process_boldi_command(message: Message):
    await message.answer(
        text='\*\_Это жирный наклонный текст\_\*:\n'
             '*_Это жирный наклонный текст_*')


# Этот хэндлер будет срабатывать на команду "/iu"
@dp.message(Command(commands='iu'))
async def process_iu_command(message: Message):
    await message.answer(
        text='\_\_\_Это наклонный подчеркнутый текст\_\\\\r\_\_:\n'
             '___Это наклонный подчеркнутый текст_\r__')


# Этот хэндлер будет срабатывать на команду "/biu"
@dp.message(Command(commands='biu'))
async def process_biu_command(message: Message):
    await message.answer(
        text='\*\_\_\_Это жирный наклонный подчеркнутый текст\_\\\\r\_\_\*:\n'
             '*___Это жирный наклонный подчеркнутый текст_\r__*')


# Этот хэндлер будет срабатывать на любые сообщения, кроме команд,
# отлавливаемых хэндлерами выше
@dp.message()
async def send_echo(message: Message):
    await message.answer(
        text='Я даже представить себе не могу, '
             'что ты имеешь в виду\n\n'
             'Чтобы посмотреть список доступных команд - '
             'отправь команду /help')


if __name__ == '__main__':
    dp.run_polling(bot)
