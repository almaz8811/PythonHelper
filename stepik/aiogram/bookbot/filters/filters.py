from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class InDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback.data, str) and callback.data.isdigit()


class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback.data, str) and 'del' \
            in callback.data and callback.data[:3].isdigit()
