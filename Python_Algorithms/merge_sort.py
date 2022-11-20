import math
from random import randint


# Merge Sort
def merging(left: list[int], right: list[int]) -> list[int]:
    # 1st argument is an iterable integer object
    # 2nd argument is an iterable integer object
    
    # Function returns a sorted iterable integer object
    new_lst = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            to_ins = right.pop(0)
            new_lst.append(to_ins)
        elif left[0] <= right[0]:
            to_ins = left.pop(0)
            new_lst.append(to_ins)
    if len(left) > 0:
        for i in left:
            new_lst.append(i)
    if len(right) > 0:
        for i in right:
            new_lst.append(i)
    return new_lst


# Sorting list with two integer elements
def merge_sort_two(lst: list[int]) -> list[int]:
    # Takes an iterable integer object as argument
    # Function returns a sorted iterable integer object
    # new_lst = []
    if len(lst) == 1:
        new_lst = lst
    else:
        left = lst[:math.floor(len(lst) / 2)]
        right = lst[math.floor(len(lst) / 2):]
        new_lst = merging(left, right)
    return new_lst


# Sorting list with four integer elements
def merge_sort_four(lst: list[int]) -> list[int]:
    if len(lst) == 1:
        new_lst = lst
    else:
        left = merge_sort_two(lst[:math.floor(len(lst) / 2)])
        right = merge_sort_two(lst[math.floor(len(lst) / 2):])
        new_lst = merging(left, right)
    return new_lst


# Sorting list with n number of elements using recursion
def merge_sort(lst: list[int]) -> list[int]:
    if len(lst) == 1:
        new_lst = lst
    else:
        left = merge_sort(lst[:math.floor(len(lst) / 2)])
        right = merge_sort(lst[math.floor(len(lst) / 2):])
        new_lst = merging(left, right)
    return new_lst


if __name__ == '__main__':
    # left_list = [1, 3, 4, 5]
    # right_list = [2, 4, 6, 7, 8]
    # print(merging(left_list, right_list))
    list_to_sort = [9, 1, 7, 3, 11, 10, 8]

    sorted_l = merge_sort(list_to_sort)
    print(sorted_l)

    # num_x = randint(-5, 10)
    # num_y = randint(-3, 7)
    # res = lambda a, b: a + b
    # print(f'{num_x} + {num_y}')
    # print(res(num_x, num_y))
    # print(abs(res(num_x, num_y)))
