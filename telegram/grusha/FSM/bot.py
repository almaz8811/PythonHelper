import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config

config: Config = load_config()


# Запуск бота
async def main():
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    # Запускаем бота и пропускаем все накопленные апдейты
    # Этот метод можно вызвать даже если включен поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
