import sys


class Gen:
    """A class that generates the squared values from 1 to n"""
    """Using dunder next method to return a generator object"""
    def __init__(self, n):
        self.nums = n
        self.last = 1

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.nums:
            raise StopIteration()
        val = self.last ** 2
        self.last += 1
        return val


# Generators
def gen(num):
    for i in range(1, num+1):
        yield i**2


def gen_1(num):
    for n in range(1, num):
        yield 1
        yield 10
        yield 100
        yield 1000


def square(num) -> list[int]:
    x = [n for n in range(num)]
    return x


if __name__ == '__main__':
    # Generators and Iterators
    mil = 1_000_000
    ten_t = 10_000
    mil_list = [i**2 for i in range(ten_t)]

    print(sys.getsizeof(mil_list))
    print(sys.getsizeof(g := gen(ten_t)))

    # for n in (x := gen(mil+1)):
    #     print(n)
    # for n in (x := gen(mil+1)):
    #     print(n)

    # while True:
    #     try:
    #         print(next(g))
    #     except StopIteration:
    #         break
    # help(Gen)
