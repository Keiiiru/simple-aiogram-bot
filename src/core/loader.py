import os
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("TOKEN"), parse_mode=ParseMode.HTML)
dp = Dispatcher()
