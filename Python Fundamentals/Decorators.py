import time


class LoopTest:
    def __init__(self, n):
        self.range_n = [n for n in range(1, n)]
        self.sample = []

    @staticmethod
    def decorate_m(func):
        """Decorator Method to time other Methods"""
        def wrapper(*args, **kwargs):
            start = time.time()
            n = func(*args)
            total = time.time() - start
            print(f'Time to run: {total}')
            return n
        return wrapper

    @decorate_m
    def loop(self):
        for i, ele in enumerate(self.range_n):
            if ele % 2 == 0:
                self.sample.append('R')
            else:
                self.sample.append('r')
        return self.sample


if __name__ == '__main__':
    l = LoopTest(10000)
    print(l.loop())





