"""Euclid's Algorithm"""
"""Getting the Greatest Common Divisor of two
non-zero or non-negative integers"""


def get_gcd(x, y):
    high = max(x, y)
    low = min(x, y)
    rm = high % low

    if rm == 0:
        return low
    if rm != 0:
        print([low, rm])
        return get_gcd(low, rm)


def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        greater += 1
    return lcm


if __name__ == '__main__':
    num_1 = int(input('1st Number: '))
    num_2 = int(input('2nd Number: '))
    print(get_gcd(num_1, num_2))
    print("LCM = ", lcm(10, 6))




