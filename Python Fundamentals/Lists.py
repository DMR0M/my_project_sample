def main():
    comprehension()
    copy()
    # nums = [12, 4, 56, 70, 2, 103, 19, 11, 64, 1, 65, 88]
    # print(sort_list(nums))
    # sort_matrix()


def slicing():
    # 1. SLICING
    # The [::] slicing takes 3 parameters [(1. start index):(2. end index or start < end):(3. intervals or-
    # step by n)]

    # This code prints the reverse of the list
    my_list = [1, 2, 3, 'x', 'y', 'z']
    reverse = my_list[::-1]
    print(reverse)

    # 2. LIST COMPREHENSIONS
    # NOTE: range()    is defined as start < end    range(1 < 11) meaning from 1 to 10
    # Define a list with the [(1. variable) (2. loop) (3. condition)]

    # This is a list that contains numbers from 1 to 10
    n_list = [i for i in range(1, 11)]
    print(n_list)

    # ** signifies exponents or ^ in calculators
    # This is a list that contains squared numbers from 1 to 10 using ** 2
    squared_list = [n**2 for n in range(1, 11)]
    print(squared_list)

    # You can also define a condition in the list comprehension
    # This list prints all even numbers ranging from 1 to 10
    # By making the condition x % 2 == 0 that will return true then it will be appended to the list as
    # (x)number otherwise it will NOT be appended to the list
    even_list = [x for x in range(1, 11) if x % 2 == 0]
    print(even_list, '\n')

    # Finding a target value in a list
    target_val = 7
    my_list = [n for n in range(1, 11) if n % 2 == 1]
    print(my_list)

    for i in range(len(my_list)):
        if my_list[i] == target_val:
            print(f'Target Found\n number of iterations: {i}')
            break
    else:
        print(f'The target {target_val} is not found')

    # Find x target
    # EXERCISE A:

    # Given an n list of integers and a target number x that matches an integer in the list.
    # Determine how many iterations in the list to find the target number.


def comprehension():
    # DEFINE A LIST BY [(1. EXPRESSION) (2. LOOP(for member in iterable)) (3. CONDITION W/O ELSE)]

    # prints each squared numbers in the list
    nums = [square(n) for n in range(1, 11)]
    print(nums)

    # prints each cubed numbers in the list
    nums = [cube(n) for n in range(1, 11)]
    print(nums)

    # nums = [cube(n) for n in range(1, 11) if n % 2 == 0]
    # print(nums)

    # prints each numbers raise to 4 in the list
    nums = [raise_4(n) for n in range(1, 11)]
    print(nums)

    # YOU CAN ALSO DEFINE A LIST BY [(1. EXPRESSION), (2. CONDITION WITH ELSE), (3. LOOP(for member in iterable))]

    # determines each numbers in the list if it is an odd or even number
    #
    filtered_nums = ['low' if i < 500 else i for i in nums]
    print(filtered_nums)


def copy():
    nums = [cube(n) for n in range(1, 11)]
    # makes a copy of the list to pass to a function to modify it
    manipulate_list(nums[:], nums)


def manipulate_list(copy_nums, nums):
    copy_nums.append(69)
    print(f'The original numbers of the list: {nums}')
    print(f'The modified numbers of the list: {copy_nums}')


# n^2 Function
def square(n):
    return n**2


# n^3 Function
def cube(n):
    return n**3


# n^4 Function
def raise_4(n):
    return n**4


# Sorting a number list
# Using the sorted method it takes a list as parameter and sorts it by default in ascending order
def sort_list(nums):
    return sorted(nums)


def sort_matrix():
    # Sort the total sum of each coordinates in the matrix in ascending order
    coordinates = [[1, -2], [2, 4], [5, -6], [-2, 11], [-5, 16], [0, 3], [8, -5]]
    # Declare {key} variable to tell what to sort and assign {key} to a lambda function to return the
    # total sum of each coordinate stored in a return variable by this expression
    # x[0] + x[1] = x -> coordinate.sort(x)
    # coordinates.sort(key=lambda x: x[0] + x[1])
    print(sorted(coordinates, key=lambda x: x[0] + x[1]))

# zip function helps you to make combinations of iterable objects
# with exactly the min. number of items
# based on the smallest iterable object


def zip_func():
    numbers_1 = [1, 1, 2, 3, 5, 8]
    numbers_2 = [2, 1, 3, 4, 9, 10, 12, 6]

    for i, j in zip(numbers_1, numbers_2):
        print(f'{i} : {j}')
    print(tuple(zip(numbers_1, numbers_2)))


def tuple_slicing():
    my_tup = ('a', 's', 9, 10, 12)
    print(my_tup[-3:-1])


def map_func():
    my_tup: tuple = (5, 6, 15, 7)
    mapped_1 = map(square, my_tup)
    mapped_list_1: list = list(mapped_1)
    my_list: list[int] = [5, 3, 12, 8]
    mapped_2 = map(lambda x: x**x, my_list)
    mapped_list_2: list = list(mapped_2)
    return mapped_list_2


if __name__ == '__main__':
    tuple_slicing()
    print(map_func())

