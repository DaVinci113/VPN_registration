import os
from loguru import logger

logger_path = "/home/proger/Programming/Real/Bots/VPN_registration/logger/debug.log"

logger.add(logger_path, format="{time} {level} {message}", level="DEBUG", rotation="100 KB", compression="zip", serialize=True)


