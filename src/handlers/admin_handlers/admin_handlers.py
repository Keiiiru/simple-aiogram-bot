from aiogram import types, F

from core.loader import dp, admin_id


@dp.message(F.text.lower() == "admin")
async def is_admin_check(m: types.Message):
    if admin_id == m.from_user.id:
        await m.answer("You're admin!")
    else:
        await m.answer("What do you mean?")
