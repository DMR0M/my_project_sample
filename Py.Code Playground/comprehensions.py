def get_data(custom_list):
    print(f'Sum of given initial list:\n{sum(custom_list)}')
    print(f'Max of given initial list:\n{max(custom_list)}')
    print(f'Min of given initial list:\n{min(custom_list)}')


def square_list(custom_list, length):
    squared_list = [custom_list[i] ** 2 for i in range(length)]
    return squared_list


def sort_list(custom_list):
    sorted_square_list = sorted(custom_list)
    return sorted_square_list


def remove_nums(custom_list, length):
    # trimmed_list = [custom_list.remove(custom_list[i]) for i in range(length) if custom_list[i] > 100]
    trimmed_list = []
    for i in range(length):
        trimmed_list.append(custom_list[i]) if custom_list[i] <= 100 else 0
    return trimmed_list


def main():
    length = int(input('type length of list: '))
    my_list = []
    for i in range(length):
        ele = int(input(f'type element of number {i + 1}: '))
        my_list.append(ele)
    squares_of_num_list = square_list(my_list, length)
    print(f'Unsorted squared list: \n{squares_of_num_list}')
    sort_list(my_list)
    sorted_num_list = sort_list(squares_of_num_list)
    print(f'Sorted squared list: \n{sorted_num_list}')
    trim_num_list = remove_nums(squares_of_num_list, length)
    print(f'Trimmed List: \n{trim_num_list}')
    get_data(my_list)


if __name__ == '__main__':
    main()
