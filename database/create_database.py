from db import DataBase
from logger.config import logger



@logger.catch
def create_database():
    """Первичная настройка БД"""

    logger.info("Создание БД начато (info)")
    with DataBase(db_file="users.db") as db:
        db.create_table()
        logger.info("Создание БД закончено (info)")


if __name__ == '__main__':
    create_database()