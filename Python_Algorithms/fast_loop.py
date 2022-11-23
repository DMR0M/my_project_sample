import timeit
import numpy


def loop(n=100_000_000):
    return numpy.sum(numpy.arange(n))


def ex_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += 1
    return s


if __name__ == '__main__':
    ele_list = [2, 5, 6, 8, 3, 9]
    print(*ele_list)
    print(f'Using Numpy\t\t {timeit.timeit(loop, number=1)}\n'
          f'{loop()}')
    print(f'Using For Loop\t\t {timeit.timeit(ex_loop, number=1)}\n'
          f'{ex_loop()}')

