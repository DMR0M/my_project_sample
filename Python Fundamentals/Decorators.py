def sample_decorator(num):
    def operation():
        print('start')
        print(num + 1)
        print('end')

    return operation()


def func1(func):
    def wrapper():
        print('first')
        func()
        print('second')

    return wrapper


@func1
def f():
    this_list: list[int] = [n for n in range(11) if n % 2 != 0]
    print(this_list)


@func1
def g():
    this_list: list[int] = [n for n in range(1, 11) if n % 2 == 0]
    print(this_list)


if __name__ == '__main__':
    f()
    g()




