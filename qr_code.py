from dotenv import load_dotenv
import os
import qrcode
from PIL import Image, ImageDraw
from setting import qr_code_path

load_dotenv()
url = os.getenv("HIDDIFY_URL")
user_proxy_path = os.getenv("PROXY_PATH_USER")


class Link:

    def __init__(self, uuid, name):
        user_url = f"https://{url}/{user_proxy_path}/{uuid}/#{name}"
        self.user_url = user_url

    def generate_qr_code(self):
        img = qrcode.make(self.user_url)
        type(img)  # qrcode.image.pil.PilImage
        img.save(qr_code_path)

    def generate_link(self):
        return self.user_url


