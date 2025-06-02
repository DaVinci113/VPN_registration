from database.db import DataBase
from setting import connecting_devices
from hiddify.request import add_free, add_premium


def add_user(user_id: int) -> str:
    with DataBase() as db:
        db.add_user(user_id)
    return "user was added"


def get_info() -> str:
    return "info about this product"


def add_devices(user_id: int, user_name: str):
    with DataBase() as db:
        user_data = db.get_user_data(user_id)
        user_data = [data for data in user_data][0]
    status = user_data[3]
    count_devices = user_data[2]
    max_count_devices = connecting_devices[status]
    if count_devices < max_count_devices:
        with DataBase() as db:
            db.add_device(user_id)
            if status:
                free_or_premium = add_premium(user_name=user_name, telegram_id=user_id)
            else:
                free_or_premium = add_free(user_name=user_name, telegram_id=user_id)
            device_id = free_or_premium['uuid']
            db.add_user_device(telegram_id=user_id, device_id=device_id)

    else:
        return "Исчерпан лимит подключений"
    return "Девайс добавлен"



def payment():
    return "make payment"