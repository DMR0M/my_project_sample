import string
from random import choice
from maskpass import advpass
from maskpass import askpass


def user_input(username, password):
    r_id = ''.join(choice(string.ascii_letters.lower()) for x in range(6))
    print(f'Username: {username} registered!\n'
          f'Password: registered!\n'
          f'Your random ID is {r_id}')

    def wrapper_user_info():
        print(f'Account Created with password: {password.advpass()}')
        return wrapper_user_info


user_name_isvalid = True
prompt_1 = input('Register a user? (y/n): ')
while user_name_isvalid:
    if prompt_1 == 'y':
        user_name = input('Type username: ')
        if len(user_name) > 15 or len(user_name) <= 3:
            user_name_isvalid = False
        pwd = askpass(prompt="Password:", mask=".")
        print(user_input(user_name, pwd))
    else:
        print('chosen to exit')
        exit()

