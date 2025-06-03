import os
from dotenv import load_dotenv
import requests
from hiddify.request_data import payload, headers
from logger.config import logger


load_dotenv()
url = os.getenv("API_URL")
proxy_path_user = os.getenv("PROXY_PATH_USER")
hiddify_url = os.getenv("HIDDIFY_URL")


@logger.catch
def add_period(user_name, telegram_id, status):
    logger.info(f"User_id {telegram_id}, Добавление периода, "
                f"user_name:{user_name}")
    payload_json= payload(user_name=user_name, telegram_id=telegram_id, status=status)
    resp = requests.post(url, json=payload_json, headers=headers)
    logger.info(f"User_id:{telegram_id}, Добавление периода, "
                f"Response:{resp} user_name:{user_name}")
    resp = resp.json()
    connect_data = {
        "id": resp["id"],
        "uuid": resp["uuid"],
        "telegram_id": resp["telegram_id"],
    }
    logger.info(f"User_id:{telegram_id}, Добавление периода "
                f"Получение данных {connect_data} "
                f"user_name {user_name}")
    return connect_data
