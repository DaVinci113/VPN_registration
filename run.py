import asyncio
import time

from aiogram import types, F
from aiogram.filters import Command
from aiogram.types import Message
from bot import dp, bot
from utils import get_info, payment, add_devices, add_user, create_and_send_link, get_str_message
from logger.config import logger
from setting import qr_code_path

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
    await message.answer(get_str_message(telegram_id=user_id))
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
    logger.debug(f"user_id::{user_id}, user_name::{user_name}")
    add = add_devices(user_id, user_name)
    await message.reply(add[0])
    if add[1]:
        uuid = add[1]["uuid"]
        create_and_send_link(uuid=uuid ,user_name=user_name)
        logger.info(f"User_id:{user_id}, QR создан")
        time.sleep(0.1)
        await bot.send_photo(message.chat.id, photo=types.FSInputFile(qr_code_path))
        logger.info(f"User_id:{user_id}, QR выслан")


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