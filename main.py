from services import auth_service
from services import db_service
import objectives

db_serv = db_service.DbService()
auth_serv = auth_service.AuthService(db_serv)

# Prompt user to login or signup
action = input('Welcome to the fitness app! Enter "1" to log in or "2" to sign up: ')
if action == '1':
    auth_serv.login()
    print("Hey there, welcome back 😄")
elif action == '2':
    auth_serv.signup()
else:
    print('Invalid input. Please try again.')

