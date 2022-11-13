def calculator(num_1, op, num_2):
    ans = 0
    error = 'Invalid operation'
    if op == '+':
        ans = num_1 + num_2
    elif op == '-':
        ans = num_1 - num_2
    elif op == '*':
        ans = num_1 * num_2
    elif op == '/':
        ans = num_1 / num_2
    else:
        return error
    return ans


def main():
    num_1 = int(input('Enter a number: '))
    op = input('Enter operation: ')
    num_2 = int(input('Enter a number: '))
    ans = calculator(num_1, op, num_2)
    print(ans)


if __name__ == "__main__":
    main()
    exit()

