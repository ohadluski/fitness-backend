from services import auth_service
from services import db_service

# from goals import Goals
db_serv = db_service.DbService()
auth_serv = auth_service.AuthService(db_serv)


# Prompt user to login or signup
action = input('Welcome to the fitness app! Enter "1" to log in or "2" to sign up: ')
if action == '1':
    auth_service.login()
    print("Hey there, welcome back 😄")
elif action == '2':
    auth_service.signup()
    auth_service.login()
else:
    print('Invalid input. Please try again.')


# print(random.choice(Breakfast))
