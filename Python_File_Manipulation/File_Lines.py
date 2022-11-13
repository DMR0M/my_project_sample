class FileReading:
    """A class that reads from files and returns as lists"""
    def __init__(self, file_path):
        self.file_path: str = file_path       # Name of file within same dir
        self.file_line_list: list[str] = []
        self.file_concat: str = ''
        self.to_float: str = ''
        self.pi_value: str = ''
        self.line_count: int = 0

    def read_from_file(self) -> list:
        # return as list
        with open(self.file_path) as file_obj:
            lines: list = file_obj.readlines()

        for line in lines:
            self.file_line_list.append(line.strip())

        return self.file_line_list

    def read_from_file_str(self) -> str:
        # return as string
        with open(self.file_path) as file_obj:
            lines: list = file_obj.readlines()

        for line in lines:
            self.file_concat += line.strip()

        return self.file_concat

    def read_from_file_int(self) -> float:
        # return as integer
        with open(self.file_path) as file_obj:
            lines: list = file_obj.readlines()

        for line in lines:
            self.to_float += line.strip()

        return float(self.to_float)

    def define_pi(self):
        with open(self.file_path) as file_obj:
            lines: list = file_obj.readlines()

        for i, line in enumerate(lines):
            self.pi_value += line.strip()
            self.line_count = i

        print(self.line_count)
        return f'{self.pi_value[:52]}'


if __name__ == '__main__':
    read_file_1 = FileReading('py_digits.txt')
    read_file_2 = FileReading('py_pi_million.txt')
    # file_data_1 = read_file_1.read_from_file()
    file_data_2 = read_file_2.read_from_file_str()
    # file_data_3 = read_file_1.read_from_file_int()
    file_data_4 = read_file_2.define_pi()

    # print(file_data_1)
    # print(len(file_data_1))
    print(file_data_2)
    # print(len(file_data_2))
    # print(file_data_3)
    print(file_data_4)
    print(len(file_data_4))
