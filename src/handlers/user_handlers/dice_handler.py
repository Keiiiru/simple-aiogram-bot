from aiogram import types
from aiogram import F

from core.loader import dp


@dp.message(F.text.lower() == "dice")
async def dice(m: types.Message):
    await m.answer_dice(emoji="🎲")
