memory = {}


def memoize_factorial(f):
    # This inner function has access to memory
    # and 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
            print('result saved in memory')
        else:
            print('returning result from saved memory')
        return memory[num]
    return inner


@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)


print(x := facto(5))
print(facto(5))
