"""Exception Handling"""


class Numbers:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def add_nums(self):
        return self.num_1 + self.num_2


if __name__ == '__main__':
    while ValueError:
        try:
            user_num1 = int(input('Type 1st number: '))
            user_num2 = int(input('Type 2nd number: '))
            my_obj = Numbers(user_num1, user_num2)
            print(my_obj.add_nums())
            break
        except ValueError:
            print('Please only input numbers')


