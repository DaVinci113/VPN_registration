import os
from dotenv import load_dotenv
import requests
from hiddify.request_data import payload_free, payload_premium, headers


load_dotenv()
url = os.getenv("API_URL")
proxy_path_user = os.getenv("PROXY_PATH_USER")
hiddify_url = os.getenv("HIDDIFY_URL")


def add_free(user_name, telegram_id):
    payload = payload_free(user_name=user_name, telegram_id=telegram_id)
    resp = requests.post(url, json=payload, headers=headers).json()
    connect_data = {
        "id": resp["id"],
        "uuid": resp["uuid"],
        "telegram_id": resp["telegram_id"],
    }
    return connect_data

def add_premium(user_name, telegram_id):
    payload = payload_premium(user_name=user_name, telegram_id=telegram_id)
    resp = requests.post(url, json=payload, headers=headers).json()

    connect_data = {
        "id": resp["id"],
        "uuid": resp["uuid"],
        "telegram_id": resp["telegram_id"],
    }
    return connect_data


# f"{hiddify_url}{proxy_path_user}/{uuid}/#{user_name}"
if __name__ == '__main__':
    print(add_free('aldkjf', 12345134))