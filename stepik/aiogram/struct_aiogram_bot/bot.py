import asyncio

from aiogram import Bot, Dispatcher
from keyboards.set_menu import set_main_menu
from config_data.config import Config, load_config
from handlers import other_handlers


# Функция конфигурирования и запуска бота
async def main():
    # Загружаем конфиг в переменную config
    config: Config = load_config()
    # Создаем объекты бота и диспетчера
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()
    # Регистрируем роутеры в диспетчере
    dp.include_router(other_handlers.router)
    # Настраиваем кнопку Menu
    await set_main_menu(bot)
    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота
    dp.startup.register(set_main_menu)
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
