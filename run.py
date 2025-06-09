import asyncio
import time

from aiogram import types, F
from aiogram.filters import Command
from aiogram.types import Message
from bot import dp, bot
from utils import get_start_message, make_subscribe, add_devices, add_user, create_and_send_link, get_user_info, make_wishes
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
        [types.KeyboardButton(text="Подписка")],
        [types.KeyboardButton(text="Пожелания")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(get_start_message())
    await message.answer("Выберете пункт в меню", reply_markup=keyboard)


@logger.catch
@dp.message(F.text.lower() == "инфо")
async def info(message: Message):
    user_id = message.from_user.id
    logger.info(f"User_id:{user_id} выбрал "
                f"инфо")
    await  message.reply(get_user_info(telegram_id=user_id))


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
        link = create_and_send_link(uuid=uuid ,user_name=user_name)
        logger.info(f"User_id:{user_id}, QR создан")
        time.sleep(0.1)
        await bot.send_photo(message.chat.id, photo=types.FSInputFile(qr_code_path))
        await message.reply(link)
        logger.info(f"User_id:{user_id}, QR выслан")


@logger.catch
@dp.message(F.text.lower() == "подписка")
async def subscribe(message: Message):
    user_id = message.from_user.id
    logger.info(f"User:{user_id} выбрал "
                f"оплатить")
    await  message.reply(make_subscribe())


@logger.catch
@dp.message(F.text.lower() == "пожелания")
async def wishes(message: Message):
    user_id = message.from_user.id
    logger.info(f"User:{user_id} выбрал "
                f"Пожелания")
    await  message.reply(make_wishes())


@logger.catch
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())