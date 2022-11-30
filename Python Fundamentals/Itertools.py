"""Itertools Module"""
# Infinite Iterators
from itertools import count
from itertools import repeat
from itertools import cycle
# Terminating Iterators
from itertools import accumulate
from itertools import chain
from itertools import compress
from itertools import pairwise
# Combinatronic Iterators
from itertools import product
from itertools import permutations
from itertools import combinations


class IteratingVal:
    def __init__(self, start, step, val):
        self.start_count = start
        self.step_count = step
        self.value = val
        self.num_list = count(self.start_count, self.step_count)
        self.sample_list = 'I Love Python'
        self.even_list: list[int] = [x for x in range(0, 50) if x % 2 == 0]
        self.odd_list: list[int] = [x for x in range(0, 50) if x % 2 != 0]
        self.count_list: list[int] = [x for x in range(1, 50)]
        self.tens_list: list[int] = [x for x in range(1, 11)]
        self.bool_list: list[bool] = [True, False, True, True, False, True]
        self.alph_list: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    """Using count"""
    # count func from itertools takes 2 arguments
    # [STARTING INDEX <i>, STEPS OR INTERVALS <j>]z
    def count_to_hundred(self):
        new_list: list[int] = []
        choice: str = input('Do you want to print as list or sequence of numbers?'
                            ' choose[1 for list/2 for sequence of nums]: ')
        if choice == '1':
            for i in self.num_list:
                if i > 100:
                    break
                new_list.append(i)
            return new_list
        if choice == '2':
            for i in self.num_list:
                if i > 100:
                    break
                new_list.append(i)
                print(i, end=" ")
        else:
            return f"Invalid input '{choice}'"

    """Using repeat"""
    # repeat func from itertools takes 2 arguments
    # [OBJECT TO REPEAT<i>, NUMBER OF TIMES TO REPEAT<j>]
    def repeat_count(self):
        list_to_repeat = repeat(self.value, self.step_count)
        for val in list_to_repeat:
            print(val, end=" ")

    """Using cycle"""
    # cycle func returns all elements of an iterable by copy
    def using_cycle(self):
        i = 0
        cycler = cycle(self.even_list)
        while i <= 50:
            print(next(cycler), end=" ")
            i += 1

    """Using chain"""
    # chains two iterable objects together as a united iterable object
    def chain_func(self):
        print(self.count_list)
        print(self.even_list)
        chained_list = chain(self.odd_list, self.even_list)
        return sorted(list(chained_list))

    """Using accumulate"""
    # accumulate func returns a list that has the sum of all elements
    # at the current position and prior
    def accumulate_obj(self):
        print(self.count_list)
        accu_list = accumulate(self.count_list)
        return list(accu_list)

    """Using compress"""
    # compress func compares two iterable objects and creates
    # a new iterable object keeping the elements if the
    # corresponding compared object's element is true
    def compress_func(self):
        compressed = compress(self.count_list, self.bool_list)
        return list(compressed)

    """Using pairwise"""
    # pairwise func pairs adjacent elements from the iterable object
    def pairwise_func(self):
        pairs = pairwise(self.count_list)
        return list(pairs)

    """Using product"""
    # returns the cartesian product of 2 iterable objects
    # equivalent to nested for loop, looping from every element
    # in iterable 1 and iterable 2
    def cartesian_product(self):
        coordinates = product(self.tens_list, self.alph_list)
        return list(coordinates)

    """Using permutations"""
    # returns using all the permutations of a particular size
    # of an iterable object
    def permute(self):
        permutation = permutations(self.alph_list, 2)
        return list(permutation)

    """Using combinations"""
    # returns all the possible combinations of a particular size
    # of an iterable object
    def combine(self):
        combination = combinations(self.alph_list, 8)
        return list(combination)


# obj_1 = IteratingVal(6, 6)
# print(obj_1.count_to_hundred())
obj_2 = IteratingVal(3, 7, 'I Love Myself')
# obj_2.repeat_count()
# obj_2.repeat_count()
print(obj_2.accumulate_obj())
# print(obj_2.chain_func())
# print(obj_2.compress_func())
# print(obj_2.pairwise_func())
# print(obj_2.cartesian_product())
# print(obj_2.permute())
# print(obj_2.combine())
# print(len(obj_2.combine()))
