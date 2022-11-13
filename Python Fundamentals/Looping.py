"""EXERCISE: TWO SUM"""
# Given an array of integers nums and a target number n return the indices
# of the numbers x and y that add up to the target


def main():
    # Prompt user to type in list's length and the numbers in the list
    length = int(input('Enter length: '))
    nums = []
    for i in range(length):
        element = int(input(f'Enter element @ index {i}: '))
        nums.append(element)
    print(nums)
    # Prompt the user to input the sum to find
    sum_of_list = int(input('Enter sum to find: '))

    # Store the returned two indices list in a list variable
    indices = two_sum(nums, sum_of_list)
    # Print the two indices in list format
    print(f'The indices that add up to the target are: {indices}')


def two_sum(n_list, target_sum):
    y = 1       # second iteration must begin in 1 for first iteration begins in 0
    # first iteration begins in 0
    for x in range(len(n_list)):
        # second iteration begins in 1
        for y in range(len(n_list)):
            # search through the two iterations' value to find if the sum of those
            # values add up to the target sum
            if n_list[x] + n_list[y] == target_sum:
                # return the values in list format
                return [x, y]
    else:
        print(f'There are no addends that add up to the sum: {target_sum}')


if __name__ == '__main__':
    main()