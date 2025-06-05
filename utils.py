from database.db import DataBase
from setting import connecting_devices, info_about_product, get_start_message
from hiddify.request import add_period
from logger.config import logger
from qr_code import Link


@logger.catch
def add_user(user_id: int) -> str:
    logger.info(f"User:{user_id}, Добавление в БД")
    with DataBase() as db:
        logger.info(f"User:{user_id}, Добавление"
                    f"Коннект с БД")
        db.add_user(user_id)
    logger.info(f"User:{user_id}, Добавление "
                f"добавлен")
    return "user was added"


@logger.catch
def get_info() -> str:
    return info_about_product

@logger.catch
def get_str_message(telegram_id):
    db = DataBase()
    result = db.get_user_data(telegram_id=telegram_id)
    status = result[-1]
    return get_start_message(status=status)

@logger.catch
def add_devices(user_id: int, user_name: str):
    logger.info(f"User_id:{user_id}, Подключение устройства, "
                f"User_name:{user_name}")
    with DataBase() as db:
        logger.info(f"User_id:{user_id}, Подключение устройства, "
                    f"Коннект с БД для добавления")
        user_data = db.get_user_data(user_id)
        user_data = [data for data in user_data][0]
    status = user_data[3]
    count_devices = user_data[2]
    logger.info(f"User_id:{user_id}, Подключение устройства, count_devices:{count_devices}")
    max_count_devices = connecting_devices[status]
    logger.info(f"User_id:{user_id}, Подключение устройства, max_count_devices:{max_count_devices}")
    if count_devices < max_count_devices:
        with DataBase() as db:
            free_or_premium = add_period(user_name=user_name, telegram_id=user_id, status=status)
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
    result = ("Успешно", {"user_id": user_id, "uuid": device_id})
    return result

@logger.catch
def create_and_send_link(uuid, user_name):
    link = Link(uuid, user_name)
    link.generate_qr_code()


@logger.catch
def payment():
    return "make payment"