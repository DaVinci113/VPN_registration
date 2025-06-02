import os
from dotenv import load_dotenv
import datetime

load_dotenv()

HIDDIFY_API_KEY = os.getenv("HIDDIFY_API_KEY")

current_date = str(datetime.date.today())

def payload_free(user_name, telegram_id):
    payload = {
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
        "package_days": 30,
        "start_date": current_date,
        "telegram_id": telegram_id,
        "usage_limit_GB": 1,
        "uuid": None,
        "wg_pk": "string",
        "wg_psk": "string",
        "wg_pub": "string"
    }
    return payload

def payload_premium(user_name, telegram_id):
    payload = {
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
        "package_days": 30,
        "start_date": current_date,
        "telegram_id": telegram_id,
        "usage_limit_GB": 100,
        "uuid": None,
        "wg_pk": "string",
        "wg_psk": "string",
        "wg_pub": "string"
    }
    return payload

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Hiddify-API-Key": HIDDIFY_API_KEY
}
