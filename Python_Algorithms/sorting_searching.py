"""Insertion Sort"""
from random import randint
from random import seed
import matplotlib.pyplot as plt
import math
import numpy as np


def insert_func(lst, ins_val):
    c_location = len(lst) - 1
    ins_location = 0
    global step_counter

    while c_location >= 0:
        step_counter += 1

        if ins_val > lst[c_location]:
            ins_location = c_location + 1
            break
        c_location -= 1
    step_counter += 1
    lst.insert(ins_location, ins_val)
    return lst


def insertion_sort(cabinet):
    new_cabinet = []
    global step_counter
    while len(cabinet) > 0:
        step_counter += 1
        to_ins = cabinet.pop(0)
        new_cabinet = insert_func(new_cabinet, to_ins)
        # print(f'{cabinet} : {new_cabinet}')
    return new_cabinet


def check_steps(size):
    cabinet = [randint(1, 1000) for n in range(size)]
    global step_counter
    step_counter = 0
    sorted_cabinet = insertion_sort(cabinet)
    return step_counter


step_counter = 0
seed(5040)
xs = list(range(1, 100))
ys = [check_steps(x) for x in xs]
xs_exp = [math.exp(x) for x in xs]
xs_squared = [x**2 for x in xs]
xs_three_halves = [x**1.5 for x in xs]
xs_cubed = [x**3 for x in xs]

plt.plot(xs, xs_exp)
plt.plot(xs, xs)
plt.plot(xs, xs_squared)
plt.plot(xs, xs_cubed)
plt.plot(xs, xs_three_halves)

ys_exp = [math.exp(x) for x in xs]
# print(ys)
plt.plot(xs, ys)

axes = plt.gca()
axes.set_ylim([np.min(ys), np.max(ys) + 140])

plt.plot(xs, ys_exp)

plt.title('comparing insertion sort to other growth rates'.title())
plt.xlabel('Number of Files in random Cabinet'.title())
plt.ylabel('Steps required to sort Cabinet'.title())
plt.show()

# a = 10
# print(a)
# b = 5
# a = b + 1
# b = -1
# print(a, b)


