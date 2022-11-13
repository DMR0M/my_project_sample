def even_or_odd_elements(num_list, length):
    bool_list = []
    for i in range(length):
        number = num_list[i]                                    # iterate numbers
        is_odd_or_even = 'Even' if number % 2 == 0 else 'Odd'   # condition to check if element i is even or odd
        bool_list.append(is_odd_or_even)                        # add the string value is_odd_or_even to the bool_list

    print(num_list)
    return bool_list


def get_num_list_elements(num_list, length):
    print(f'The list has {length} elements')
    print(num_list)


def get_product_of_list(num_list):
    product = 1
    for i in range(len(num_list)):
        product *= num_list[i]

    return product


def get_average_of_list(num_list, length):
    sum = 0
    for i in range(length):
        sum += num_list[i]
    average = sum/length
    return average


def get_max(num_list, length):
    max_num = num_list[0]
    for i in range(length):
        max_num = num_list[i] if max_num < num_list[i] else 0
    return max_num


def get_difference_of_list(num_list, length):
    diff = get_max(num_list, length)
    for i in range(length):
        if num_list[i] != diff:
            diff -= num_list[i]
    print(f'The answer is {diff}')


def get_ave_of_list_while_loop(num_list, length):
    sum = 0
    i = 0
    while i < length:
        sum += num_list[i]
        i += 1
    average = sum/length
    return average


def sorted_method(num_list):
    sort_num_list = sorted(num_list)
    return sort_num_list


def args_and_kwargs(a, b, c, d):
    print(f'{a}->{b}->{c}->{d}')


def main(word_list):
    joint = ', '.join(word_list)
    print(joint)


# length_of_list = int(input("Type list's length: "))
# number_list = []
# for i in range(length_of_list):
    # elements = int(input(f'Type element at index {i}: '))
    # number_list.append(elements)

# ave = get_ave_of_list_while_loop(number_list, length_list)
# print(f'The average of the numbers in the list {ave}')

# get_difference_of_list(number_list, length_of_list)

word = ['Rommel', 'RR', 'Rudolf', 'Dela Merced', 'Amoloza']
my_dict = {1: 'Rommel', 2: 'Cyrelle', 3: 'Lance', 4: 'Marck', 5: 'Kevin'}
name = 'Rommel' [::-1]

if __name__ == '__main__':
    list_of_motorcycles = ['yamaha', 'suzuki', 'honda', 'ducati']
    print(*list_of_motorcycles)
    print(name)

exit()



