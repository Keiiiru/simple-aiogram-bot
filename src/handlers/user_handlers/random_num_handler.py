from random import randint

from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.loader import dp


@dp.message(F.text.lower() == "choice random number")
async def random_number_message(m: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(text="Click me", callback_data="random_value")
    )
    await m.answer(
        "Click the button, if u wanna get a random number",
        reply_markup=builder.as_markup(),
    )


@dp.callback_query(F.data == "random_value")
async def random_num_callback_query(cb: types.CallbackQuery):
    await cb.message.answer(str(randint(1, 10)))
