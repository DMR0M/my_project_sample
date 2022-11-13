import string
from secrets import choice
n = 9


def sample_sort(word):
    rev = word[::-1]
    return rev


def joining():
    a_list = string.ascii_letters + string.digits
    password = ''.join(choice(a_list) for i in range(10))
    print(a_list)
    print(password)


if __name__ == '__main__':
    joining()
