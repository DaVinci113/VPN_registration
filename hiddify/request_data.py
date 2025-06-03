import os
from dotenv import load_dotenv
import datetime
from setting import free_or_premium
from logger.config import logger

load_dotenv()

HIDDIFY_API_KEY = os.getenv("HIDDIFY_API_KEY")


@logger.catch
def payload(user_name, telegram_id, status):

    current_date = str(datetime.date.today())

    gb = free_or_premium[status]["GB"]
    days = free_or_premium[status]["days"]

    payload_period = {
        "added_by_uuid": "ME",
        "comment": None,
        "current_usage_GB": 0,
        "ed25519_private_key": "string",
        "ed25519_public_key": "string",
        "enable": True,
        "is_active": True,
        "lang": "ru",
        "last_online": None,
        "last_reset_time": None,
        "mode": "monthly",
        "name": user_name,
        "package_days": days,
        "start_date": current_date,
        "telegram_id": telegram_id,
        "usage_limit_GB": gb,
        "uuid": None,
        "wg_pk": "string",
        "wg_psk": "string",
        "wg_pub": "string"
    }
    logger.info(f"User_id {telegram_id}, Добавление периода, GB:{gb} DAYS:{days}  "
                f"user_name:{user_name}")
    return payload_period


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Hiddify-API-Key": HIDDIFY_API_KEY
}
