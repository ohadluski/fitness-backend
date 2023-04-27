import sqlite3
# import csv
import consts


def users_table():
    conn = sqlite3.connect("../users.db")
    cursor = conn.cursor()

    sql = (F'''
        CREATE TABLE IF NOT EXISTS {consts.TableNames.USERS} (
            username TEXT PRIMARY KEY,
            password TEXT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            gender TEXT,
            phone_number INTEGER,
            address TEXT,
            age INTEGER,
            weight INTEGER,
            height INTEGER,
            calorie_count INTEGER
        )
    ''')

    cursor.execute(sql)
    print("Database has been created successfully")


class DbService:
    def __init__(self):
        self.conn = sqlite3.connect(consts.DATABASE_FILE)
        self.cursor = self.conn.cursor()

    def execute(self, query: str):
        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.fetchall()