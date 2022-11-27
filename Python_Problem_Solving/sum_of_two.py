"""EXERCISE: TWO SUM"""
# Given an array of integers nums and a target number n return the indices
# of the numbers x and y that add up to the target


def main():
    # Length of the list and the elements
    length = int(input("Type the list's length: "))
    nums = []
    for i in range(length):
        elem = int(input(f'Enter element @ index {i}: '))
        nums.append(elem)

    # Display and prompt target sum
    print(f'The elements in the list are: \n{nums}')
    target = int(input('Type the target sum: '))
    indices = return_indices(nums, target)
    print(f'The indices are {indices}')


def return_indices(nums, target):
    # Find with two iterators
    for x in range(len(nums)):
        for y in range(1, len(nums)):
            # Check if the iterated value x and y add up to the target sum
            if nums[x] + nums[y] == target:
                # Return those indices as a list
                return [x, y]


if __name__ == '__main__':
    main()
