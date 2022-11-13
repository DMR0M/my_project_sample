# Import a Class and a function from the same directory to a python file
from Arithmetics import Arithmetic


def do_math():
    print(Arithmetic.add(9, 10))
    print(Arithmetic.subtract(5, 10))
    print(Arithmetic.add(23324, 21349))
    print(Arithmetic.cube(7))
    print(Arithmetic.multiply(7, 19))
    print(Arithmetic.divide(90, 50))


def game():
    ans = input('Type answer: ')
    options = ['rock', 'paper', 'scissors']
    print('yey') if ans in options else game()


if __name__ == '__main__':
    do_math()
    game()

