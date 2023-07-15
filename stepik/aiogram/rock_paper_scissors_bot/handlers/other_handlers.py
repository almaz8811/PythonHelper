from aiogram import Router
from aiogram.types import Message
from stepik.aiogram.rock_paper_scissors_bot.lexicon.lexicon_ru import LEXICON_RU

router: Router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
