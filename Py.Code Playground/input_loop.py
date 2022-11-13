def options(num):
    user_input: int = 0
    while user_input != 4:
        user_input = int(input('What would you like to do? '))
        if user_input == 1:
            print('You chose + 1')
            return num + 1
        elif user_input == 2:
            print('You chose + 2')
            return num + 2
        elif user_input == 3:
            print('You chose + 3')
            return num + 3
        elif user_input == 4:
            pass
        else:
            print("That is not a valid input.")
    exit()


if __name__ == '__main__':
    n: int = 9
    ope = options(n)
    print(ope)
