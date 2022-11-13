"""Get user inputted full name"""
from format_name import get_user_fullname


print('Enter q to quit at anytime')
while True:
    first = input('\nPlease enter first name: ')
    if first == 'q':
        break
    last = input('\nPlease enter last name: ')
    if last == 'q':
        break

    formatted_name = get_user_fullname(first, last)
    print(f'\nFormatted Name: {formatted_name}')