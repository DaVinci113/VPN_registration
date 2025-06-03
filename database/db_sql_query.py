create_table_users = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER NOT NULL,
        connecting_devices INTEGER DEFAULT 0,
        status BOOLEAN DEFAULT FALSE
        );"""

create_table_users_device = """CREATE TABLE IF NOT EXISTS users_device (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        connecting_devices INTEGER,
        telegram INTEGER,
        FOREIGN KEY (telegram) REFERENCES users (telegram_id) ON DELETE CASCADE
        );"""

insert_client = """
INSERT INTO users (telegram_id)
VALUES (?);
"""

select_client = """
SELECT telegram_id
FROM users
WHERE telegram_id=?;
"""

select_users_device = """
SELECT telegram_id
FROM users_device
WHERE telegram_id=?;
"""

add_device = """
UPDATE users
SET connecting_devices=connecting_devices+1
WHERE telegram_id=?;
"""

add_user_device = """
INSERT INTO users_device (connecting_devices, telegram)
VALUES (?,?);
"""

get_user_data = """
SELECT *
FROM users
WHERE telegram_id=?;
"""
