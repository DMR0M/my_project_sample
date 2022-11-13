import numpy as np
from itertools import chain


class NumPy:
    def __init__(self):
        self.li_1 = [1, 2, 3]
        self.li_2 = [4, 5, 6]
        self.arr_1 = np.array([1, 2, 3])
        self.arr_2 = np.array([4, 5, 6])

    def add_arrays(self):
        return self.arr_1 + self.arr_2

    def add_lists(self):
        # chaining = chain(self.li_1, self.li_2)
        # return list(chaining)
        return self.li_1 + self.li_2


obj_1 = NumPy()
print(obj_1.add_arrays())
print(obj_1.add_lists())

