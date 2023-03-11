# Import necessary modules
import csv
from os import system
import sqlite3
import consts
from services import db_service


# Define a class for the fitness app
class AuthService:
    def __init__(self, db: db_service.DbService):
        """ Load user data from CSV file"""
        self.db = db

    def login(self):
        logged_in = False
        # Check if user exists and password is correct
        while not logged_in:
            username = input('Username: ')
            username_query = f" SELECT * FROM {consts.TableNames.USERS} WHERE username = '{username}'"
            user_check = self.db.execute(username_query)
            if len(user_check) > 0:
                password = input('Password: ')
                password_query = f" SELECT * FROM {consts.TableNames.USERS} WHERE password = '{password}'"
                pass_check = self.db.execute(password_query)
                if len(pass_check) == 0:
                    print("Wrong Password. Please try again")
                else:
                    logged_in = True
            else:
                print("User Does not Exists. Please try again.")

        print("Login Successful!")



    def signup(self):
        # Prompt user for signup information
        username = input('Choose a username: ')
        password = "1234" # input('Choose a password: ')
        first_name = "ohad" #input('Enter your first name: ')
        last_name = "luski" # input('Enter your last name: ')
        email = "luskioh@gmail.com" #input('Enter your email address: ')
        gender = "male" #input('Enter your gender: ')
        phone_number = "123" # input('Enter your phone number: ')
        address = "street" # input('Enter your address: ')
        age = 29 # input('Enter your age: ')
        weight = 80 #input('Enter your weight (in kg): ')
        height = 180 # input('Enter your height (in cm): ')
        calorie_count = 0

        # Adds user to the database
        query = f"INSERT INTO {consts.TableNames.USERS} values ('{username}', '{password}', '{first_name}', '{last_name}', '{email}', " \
                f"'{gender}','{phone_number}', '{address}', {age}, {weight}, {height}, {calorie_count})"
        try:
            self.db.execute(query)
            print("Signed Up Successfully!")
        except sqlite3.IntegrityError:
            print("User already exists. Try again.")
            self.signup()







        # self.users[username] = {'username': username, 'password': password, 'first_name': first_name,
        #                         'last_name': last_name, 'email': email, 'gender': gender, 'phone_number': phone_number,
        #                         'address': address, 'age': age, 'weight': weight, 'height': height,
        #                         'calorie_count': calorie_count}
        # fieldnames = ['username', 'password', 'first_name', 'last_name', 'email', 'gender', 'phone_number', 'address',
        #               'age', 'weight', 'height', 'calorie_count']
        # with open('../users.csv', 'w', newline='') as f:
        #     writer = csv.DictWriter(f, fieldnames=fieldnames)
        #     writer.writeheader()
        #     writer.writerows(self.users.values())
        #
        # system("clear")
        # print('Signup successful! Please log in.')