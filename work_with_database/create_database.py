from logger.config import logger
from db import DataBase



@logger.catch
def create_database():
    """Первичная настройка БД"""

    logger.info("Создание БД начато (info)")
    with DataBase(db_file="database/users.db") as dtb:
        dtb.create_table()
        logger.info("Создание БД закончено (info)")


if __name__ == '__main__':
    create_database()