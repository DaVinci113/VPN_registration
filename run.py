import asyncio
from aiogram import types, F
from aiogram.filters import Command
from aiogram.types import Message
from bot import dp, bot
from utils import get_info, payment, add_devices, add_user
from hiddify.request import add_free


@dp.message(Command("start"))
async def cmd_start(message: Message):
    user_id = message.from_user.id
    add_user(user_id)
    kb = [
        [types.KeyboardButton(text="ИНФО")],
        [types.KeyboardButton(text="Подключить устройство")],
        [types.KeyboardButton(text="Оплатить")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Выберете пункт в меню", reply_markup=keyboard)


@dp.message(F.text.lower() == "инфо")
async def info(message: Message):
    await  message.reply(get_info())


@dp.message(F.text.lower() == "подключить устройство")
async def add_device(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    await message.reply(add_devices(user_id, user_name))


@dp.message(F.text.lower() == "оплатить")
async def make_payment(message: Message):
    await  message.reply(payment())


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())