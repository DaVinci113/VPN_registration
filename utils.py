from database.db import DataBase
from setting import connecting_devices, start_message, get_info, send_qr, send_link
from hiddify.request import add_period
from logger.config import logger
from qr_code import Link


@logger.catch
def add_user(user_id: int) -> str:
    """Добавление пользователя"""

    logger.info(f"User:{user_id}, Добавление в БД")
    with DataBase() as db:
        logger.info(f"User:{user_id}, Добавление"
                    f"Коннект с БД")
        db.add_user(user_id)
    logger.info(f"User:{user_id}, Добавление "
                f"добавлен")
    return "user was added"


@logger.catch
def get_start_message() -> str:
    """Сообщение при старте бота"""

    return start_message

@logger.catch
def get_user_info(telegram_id: int) -> str:
    """Инфо по тарифу пользователя"""

    db = DataBase()
    result = db.get_user_data(telegram_id=telegram_id)
    status = result[-1]
    return get_info(status=status)

@logger.catch
def add_devices(user_id: int, user_name: str) -> tuple[str, dict]:
    """Добавление устройства"""

    logger.info(f"User_id:{user_id}, Подключение устройства, "
                f"User_name:{user_name}")
    with DataBase() as db:
        logger.info(f"User_id:{user_id}, Подключение устройства, "
                    f"Коннект с БД для добавления")
        user_data = db.get_user_data(user_id)
        logger.debug(f"user_data :: {user_data}")
        logger.debug(f"user_data_list:: {user_data}")
    status = user_data[3]
    count_devices = user_data[2]
    logger.info(f"User_id:{user_id}, Подключение устройства, count_devices:{count_devices}")
    max_count_devices = connecting_devices[status]
    logger.debug(f"status::{status}")
    logger.info(f"User_id:{user_id}, Подключение устройства, max_count_devices:{max_count_devices}")
    if count_devices < max_count_devices:
        with DataBase() as db:
            free_or_premium = add_period(user_name=user_name, telegram_id=user_id, status=status)
            logger.debug(f"free_or_premium :: {free_or_premium}")
            logger.info(f"User_id:{user_id}, Подключение устройства, user_status:{status} add period")
            device_id = free_or_premium['uuid']
            db.add_device(user_id)
            db.add_user_device(telegram_id=user_id, device_id=device_id)
            logger.info(f"User_id:{user_id}, Подключение устройства, device_id:{device_id}")
    else:
        result = ("Исчерпан лимит подключений", {})
        logger.info(f"User_id:{user_id}, Подключение устройства, {result}")
        return result
    logger.info(f"User_id:{user_id}, Подключение устройства, device_id:{device_id}, OK")
    result = (send_qr, {"user_id": user_id, "uuid": device_id})
    return result

@logger.catch
def create_and_send_link(uuid: int, user_name: str) -> str:
    """Создание и отправка qr и ссылки"""
    link = Link(uuid, user_name)
    link.generate_qr_code()
    return f"{send_link}\n{link.generate_link()}"


@logger.catch
def payment():
    """Платеж"""
    return "make payment"