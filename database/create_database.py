from db import DataBase


def create_database():
    with DataBase(db_file="users.db") as db:
        db.create_table()

if __name__ == '__main__':
    create_database()