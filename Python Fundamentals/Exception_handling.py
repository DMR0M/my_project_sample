# Person Information Input Validation
# Simple Program

def age_validation(name, age):
    message_1 = f'{age} - You are a minor'
    message_2 = f'{age} - You are not a minor'
    print(message_1) if age < 18 else print(message_2)


error_message = 'An error occured'


def error_func():
    print('Invalid syntax for name')


try:
    name = input("Type your name: ")
    for i in name:
        if i.isdigit():
            error_func()
            exit()

    age = int(input('Type your age: '))
    age_validation(name, age)

except ValueError as ve:
    print(ve)

# Type of Exceptions are:
    # - TypeError
    # - ValueError
    # - SyntaxError
    # - ZeroDivisionError

# Assert Method


def input_number(num):
    # If num is not less than 50 call AssertionError
    assert num > 50, f'Number must not be less than 50 {num=}'


given_num = int(input('Type a number: '))
input_number(given_num)

set_1 = {1, 2, 3, 4, 5}
set_2 = {5, 6, 7, 8, 9}

print(tuple(set_1 & set_2))

