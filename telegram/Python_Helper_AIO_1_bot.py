from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
import os


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}. Рад тебя видеть!')
    await message.answer(f'Привет {message.from_user.first_name}. Рад тебя видеть!')
    await message.reply(f'Привет {message.from_user.first_name}. Рад тебя видеть!')


async def start():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher(bot)
    dp.register_message_handler(get_start)
    try:
        await dp.start_polling()
    finally:
        bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
