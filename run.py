import asyncio
from aiogram import types, F
from aiogram.filters import Command
from aiogram.types import Message
from bot import dp, bot
from utils import get_info, payment, add_devices, add_user
from logger.config import logger


@logger.catch
@dp.message(Command("start"))
async def cmd_start(message: Message):
    user_id = message.from_user.id
    logger.info(f"User_id:{user_id} start bot")
    add_user(user_id)
    kb = [
        [types.KeyboardButton(text="ИНФО")],
        [types.KeyboardButton(text="Подключить устройство")],
        [types.KeyboardButton(text="Оплатить")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Выберете пункт в меню", reply_markup=keyboard)


@logger.catch
@dp.message(F.text.lower() == "инфо")
async def info(message: Message):
    await  message.reply(get_info())


@logger.catch
@dp.message(F.text.lower() == "подключить устройство")
async def add_device(message: Message):
    user_id = message.from_user.id
    logger.info(f"User:{user_id} выбрал "
                f"Подключение устройства")
    user_name = message.from_user.full_name
    await message.reply(add_devices(user_id, user_name))


@logger.catch
@dp.message(F.text.lower() == "оплатить")
async def make_payment(message: Message):
    user_id = message.from_user.id
    logger.info(f"User:{user_id} выбрал "
                f"оплатить")
    await  message.reply(payment())


@logger.catch
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())