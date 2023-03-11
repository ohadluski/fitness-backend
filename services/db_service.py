import sqlite3
import csv
import consts


def create_table():
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


# def push_csv_data_to_sqlite(users_csv):
#     with open(users_csv, 'r') as f:
#         next(f) # Skip the header row.
#         reader = csv.reader(f)
#         for row in reader:
#             cursor.execute('''
#                 INSERT INTO users_db (username, password, first_name, last_name, email, gender, phone_number, address,
#                 age, weight, height, calorie_count)
#                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#             ''', row)
#
#
# for row in cursor.execute("SELECT DISTINCT * FROM users_db WHERE username = 'ohadluski'"):
#     print(row, "\n")
#
# conn.commit()
# conn.close()


# Create functions for each logic and call those functions when appropriate
