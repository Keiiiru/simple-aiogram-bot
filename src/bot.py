import asyncio

from aiogram import types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from core.loader import bot, dp
from handlers import setup_handlers


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = ReplyKeyboardBuilder()
    kb.row(types.KeyboardButton(text="dice"), types.KeyboardButton(text="developed by"))
    kb.row(types.KeyboardButton(text="choice random number"))
    kb.row(
        types.KeyboardButton(text="get location", request_location=True),
        types.KeyboardButton(text="get contact", request_contact=True),
    )

    await message.answer(
        "Hi! \n \n \n I'm example bot written on aiogram 3",
        reply_markup=kb.as_markup(resize_keyboard=True),
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    setup_handlers()

    asyncio.run(main())
