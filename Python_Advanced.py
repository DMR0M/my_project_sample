import sys
from dataclasses import dataclass


@dataclass(kw_only=True)
class List:
    list_of_num: list


@dataclass(kw_only=True)
class Generator:
    """Understand Generators"""
    gen_list_of_num: list


def print_list():
    list_ = List(list_of_num=[n for n in range(1000000)])
    return list_


def print_gen_obj():
    gen = Generator(gen_list_of_num=[n for n in range(1000000)])
    yield gen


@dataclass()
class Fibonacci:
    x: int = 0
    y: int = 1


def apply_fibonacci(limit):
    a = Fibonacci()
    while a.x < limit:
        yield a
        a.x, a.y = a.y, a.x + a.y


def fibonacci(range):
    a: int = 0
    b: int = 1
    while a < range:
        yield a
        a, b = b, a + b


def return_fib(range):
    a: int = 0
    b: int = 1
    while a < range:
        a, b = b, a + b
        return a


def compare(limit: int):
    common_list = [i for i in range(1, limit)]
    generator_list = (x for x in range(1, limit))
    print(sys.getsizeof(common_list))
    print(sys.getsizeof(generator_list))


if __name__ == '__main__':
    n_limit: int = int(input('Type number limit: '))
    compare(n_limit)
    # fib = apply_fibonacci(n_limit)
    # fib = fibonacci(n_limit)
    # fib_1 = return_fib(n_limit)
    # for i in fib:
    #    print(f'{i} ', end='')
    print('\n')
    # print(sys.getsizeof(fib))

    # print(sys.getsizeof(print_list()))
    # print(sys.getsizeof(print_gen_obj()))


