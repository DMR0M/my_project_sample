"""Json Dump and Load"""

import json


def store_data(username, filename):
    with open(filename, 'a') as file:
        json.dump(username, file)
        print(f'We will remember you {username}!')


if __name__ == '__main__':
    filename = 'users.json'
    username = input('Please input your name: ')
    store_data(username, filename)
