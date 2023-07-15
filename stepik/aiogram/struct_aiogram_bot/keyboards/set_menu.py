from aiogram import Bot
from aiogram.types import BotCommand

from stepik.aiogram.struct_aiogram_bot.lexicon.lexicon_ru import LEXICON_COMMANDS_RU


# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки Menu
    main_menu_commands = [
        BotCommand(command=command, description=description) for command, description in LEXICON_COMMANDS_RU.items()
    ]
    await bot.set_my_commands(main_menu_commands)
