import sqlite3
from database.db_sql_query import create_table_users, create_table_users_device, add_device, insert_client, \
    select_client, get_user_data, add_user_device


class DataBase:

    def __init__(self, db_file="database/users.db"):
        self._conn = sqlite3.connect(db_file)
        self._cur = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cur

    def commit(self):
        self.connection.commit()

    def create_table(self):
        self.cursor.execute(create_table_users)
        self.cursor.execute(create_table_users_device)
        self.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.cursor.close()
        self.connection.close()

    def check_user(self, telegram_id: int):
        try:
            user = self.cursor.execute(select_client, (telegram_id,))
            user_exist = user.fetchone()
            return bool(user_exist)
        except Exception as ex:
            return False

    def add_user(self, telegram_id: int):
        if not self.check_user(telegram_id):
            self.cursor.execute(insert_client, (telegram_id,))

    def get_user_data(self, telegram_id: int):
        return self.cursor.execute(get_user_data, (telegram_id,))

    def add_device(self, telegram_id: int):
        self.cursor.execute(add_device, (telegram_id,))

    def add_user_device(self, device_id, telegram_id):
        self.cursor.execute(add_user_device, (device_id, telegram_id,))
