from aiogram import types
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.loader import dp


@dp.message(F.text.lower() == "developed by")
async def developed_by(m: types.Message):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        types.InlineKeyboardButton(text="Chris Deviskonty", url="https://t.me/Mwossw")
    )
    await m.answer("i'm delveloped by:", reply_markup=keyboard.as_markup())
