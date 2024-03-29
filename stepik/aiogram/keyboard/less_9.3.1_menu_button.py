from aiogram import Bot, Dispatcher
from aiogram.types import Message, BotCommand
from aiogram.filters import Command, Text
from config_data.config import Config, load_config

config: Config = load_config()

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()


# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки Menu
    main_menu_commands = [
        BotCommand(command='/help', description='Справка по работе бота'),
        BotCommand(command='/support', description='Поддержка'),
        BotCommand(command='contacts', description='Другие способы связи'),
        BotCommand(command='/payments', description='Платежи'),
        BotCommand(command='/delmenu', description='Удалить меню')
    ]
    await bot.set_my_commands(main_menu_commands)


'''
Пояснение по инструкции dp.startup.register(set_main_menu). Таким способом можно регистрировать в диспетчере функции, 
которые должны выполняться при старте бота. По сути, это способ добавить функцию в событийный цикл средствами aiogram, 
не обращаясь напрямую к asyncio. Причем, функция эта может быть как синхронной, так и асинхронной, aiogram сам 
разберется как ее выполнить.
'''


# Этот хэндлер будет срабатывать на /delmenu
# и удалять кнопку Menu с командами
@dp.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка Menu удалена')


if __name__ == '__main__':
    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота
    dp.startup.register(set_main_menu)
    # Запускаем поллинг
    dp.run_polling(bot)
