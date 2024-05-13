from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State, default_state

from telegram.grusha.FSM.keyboards.simple_row import make_row_keyboard

available_food_names = ['Суши', 'Спагетти', 'Хачапури']
available_food_sizes = ['Маленькую', 'Среднюю', 'Большую']


class OrderFood(StatesGroup):
    choosing_food_name = State()
    choosing_food_size = State()


router = Router()


@router.message(StateFilter(default_state), Command('food'))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer(text='Выберите блюдо:', reply_markup=make_row_keyboard(available_food_names))
    # Устанавливаем пользователю состояние 'выбирает название'
    await state.set_state(OrderFood.choosing_food_name)
