from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from telegram.grusha.routers.keyboards.for_questions import get_yes_no_kb

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Сделать проверку?', reply_markup=get_yes_no_kb())


@router.message(F.text.lower() == 'да')
async def answer_yes(message: Message):
    await message.answer('Хорошо', reply_markup=ReplyKeyboardRemove())


@router.message(F.text.lower() == 'нет')
async def answer_no(message: Message):
    await message.answer('Понятно', reply_markup=ReplyKeyboardRemove())
