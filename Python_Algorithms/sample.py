import matplotlib.pyplot as plt
import numpy as np


class CreateGraph:
    def __init__(self, x, y):
        self.x_val = x
        self.y_val = y

    def show(self):
        plt.plot(self.x_val, self.y_val)
        plt.title('this is a sample graph'.title())
        plt.show()
        # plt.xlabel('')
        # plt.ylabel('')


if __name__ == '__main__':
    x_arr = np.array([x**2 for x in range(10)])
    y_arr = np.array([x**3 for x in range(10)])
    c = CreateGraph(x_arr, y_arr)
    c.show()

# def ins_sort(lst: list[int]) -> list[int]:
#     new_lst = []
#     while len(lst) > 0:
#         to_ins = lst.pop(0)
#         new_lst = ins_func(new_lst, to_ins)
#         # print(f'{cabinet} : {new_cabinet}')
#     return new_lst
