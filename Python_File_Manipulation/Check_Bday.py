from File_Lines import FileReading

if __name__ == '__main__':
    def check(x) -> bool:
        check_birthday: str = input('Type your birthday format(mm/dd/yy): ')
        if check_birthday in pi_string:
            return True
        return False

    file_data = FileReading('py_pi_million.txt')
    pi_string: str = file_data.read_from_file_str()
    print(check(pi_string))

    ex_dict = {1: 'RR', 2: 'Joko', 3: 'Rudy'}
    for i in ex_dict:
        print(f'{i}: {ex_dict[i]}', end='  ')
    print(f'\n{ex_dict}')

