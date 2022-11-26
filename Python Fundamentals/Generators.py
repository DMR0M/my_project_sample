
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


def gen(num):
    for i in range(num):
        yield i**2


def square(num):
    for i in range(num):
        print(i**2)


if __name__ == '__main__':
    mil = 1_000_000

    # for n in (x := gen(mil+1)):
    #     print(n)
    for n in (x := gen(mil+1)):
        print(n)

    # while True:
    #     try:
    #         print(next(g))
    #     except StopIteration:
    #         break
    # help(Gen)
