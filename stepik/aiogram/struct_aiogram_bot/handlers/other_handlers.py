from aiogram import Router, Bot
from aiogram.filters import Command, Text
from aiogram.types import Message

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на /delmenu
# и удалять кнопку Menu с командами
@router.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка Menu удалена')
