from aiogram import types
from aiogram.filters import Command
from aiogram.types import Message

from bot import dp


@dp.massage(Command("start"))
async def cmd_start(message: Message):
    kb = [
        [types.KeyboardButton(text="ИНФО")],
        [types.KeyboardButton(text="Подключить устройство")],
        [types.KeyboardButton(text="Оплатить")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Выберете пункт в меню", reply_markup=keyboard)