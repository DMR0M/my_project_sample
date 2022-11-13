def int_to_roman_nums(x):
    nums_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_nums_list = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    i = len(nums_list) - 1
    roman_num = ''
    while x != 0:
        if nums_list[i] <= x:
            roman_num += roman_nums_list[i]     # append roman_num with the highest number in the roman list
            x = x - nums_list[i]
        else:
            i -= 1
    return roman_num


def main():
    number = int(input('Type a number: '))
    num_to_roman = int_to_roman_nums(number)
    print(num_to_roman)


if __name__ == '__main__':
    main()