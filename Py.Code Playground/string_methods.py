def print_string(name):
    message = F'Welcome {name}!'
    # returns each string value in title format(first letter in each string is
    # converted to uppercase)
    print(message.title())


def get_user_name():
    u_name = input('Type first and last name: ')

    print_string(u_name)


get_user_name()