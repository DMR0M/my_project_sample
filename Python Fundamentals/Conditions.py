MESSAGE = 'PASSWORD CREATED SUCCESSFULLY'
PROMPT = 'PASSWORD DOES NOT MATCH'

def main():
    user_input()


# 1. TERNARY CONDITIONS
def ternary():
    age = int(input('Enter your age: '))
    check = True if age < 18 else False
    print(f'Are you a Minor?\n{check}')


# 2. Recursion
def user_input():
    make_password = input('Create a password: ')
    valid_password = input('Type password again: ')
    user_input() if make_password != valid_password else login(make_password)


def login(password):
    login_password = input('Type the password: ')
    print('ACCESS GRANTED') if login_password == password else print('Wrong password'), login(password)


if __name__ == '__main__':
    main()
