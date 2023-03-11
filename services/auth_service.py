# Import necessary modules
import csv
from os import system
from services import db_service


# Define a class for the fitness app
class AuthService:
    def __init__(self, db: db_service.DbService):
        """ Load user data from CSV file"""
        self.db = db
        self.db.execute()
        with open('../users.csv', newline='') as f:
            reader = csv.DictReader(f)
            self.users = {row['username']: row for row in reader}

    def login(self):
        logged_in = False
        """ Check if user exists and password is correct"""
        while not logged_in:
            username = input('Username: ')
            password = input('Password: ')
            if username in self.users and self.users[username]['password'] == password:
                system("clear")
                print('Login successful!')
                logged_in = True
            else:
                system("clear")
                print('Incorrect username or password. Please try again.')
        return logged_in

    def signup(self):
        """ Prompt user for signup information"""
        username = input('Choose a username:  ')
        password = input('Choose a password: ')
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        email = input('Enter your email address: ')
        gender = input('Enter your gender: ')
        phone_number = input('Enter your phone number: ')
        address = input('Enter your address: ')
        age = input('Enter your age: ')
        weight = input('Enter your weight (in kg): ')
        height = input('Enter your height (in cm): ')
        calorie_count = 0

        """ Add user to dictionary and save to CSV file"""
        self.users[username] = {'username': username, 'password': password, 'first_name': first_name,
                                'last_name': last_name, 'email': email, 'gender': gender, 'phone_number': phone_number,
                                'address': address, 'age': age, 'weight': weight, 'height': height,
                                'calorie_count': calorie_count}
        fieldnames = ['username', 'password', 'first_name', 'last_name', 'email', 'gender', 'phone_number', 'address',
                      'age', 'weight', 'height', 'calorie_count']
        with open('../users.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.users.values())

        system("clear")
        print('Signup successful! Please log in.')
