import asyncio
from aiogram import Bot, Dispatcher
from handlers import questions, different_types

from config_data.config import Config, load_config

config: Config = load_config()


# Запуск бота
async def main():
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    # dp.include_routers(questions.router, different_types.router) - вариант в одну строку
    dp.include_router(questions.router)
    dp.include_router(different_types.router)
    # Запускаем бота и пропускаем все накопленные апдейты
    # Этот метод можно вызвать даже если включен поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
