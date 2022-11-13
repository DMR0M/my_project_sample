import math


def binary_search(lst, x):
    guess = math.floor(len(lst)/2)
    upper = len(lst)
    lower = 0
    while abs(lst[guess] - x) > 0.0001:
        if lst[guess] > x:
            upper = guess
            guess = math.floor((guess + lower)/2)
        if lst[guess] < x:
            lower = guess
            guess = math.floor((guess + upper) / 2)
    return f'The sorted list: {lst}\nThe index of the target is: {guess}'


if __name__ == '__main__':
    my_lst = [14, 9, 10, 11, 13, 4, 5]
    s_lst = sorted(my_lst)
    target = 13
    # print(s_lst)
    print(binary_search(s_lst, target))
