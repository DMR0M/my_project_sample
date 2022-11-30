from dataclasses import dataclass, field


@dataclass()
class RemoveComments:
    file_in: str
    file_out: str
    content: list[str] = field(init=False)
    new_content = []

    def show_content(self) -> list[str]:
        with open(self.file_in) as f:
            self.content = f.readlines()
        return self.content

    def read_file(self) -> list[str]:
        with open(self.file_in) as f:
            self.content = f.readlines()
            for i, ele in enumerate(self.content):
                if ('*' or '/') not in ele:
                    self.new_content.append(ele)
            return self.new_content

    def write_new_file(self) -> None:
        with open(self.file_out, 'w') as f:
            for i, ele in enumerate(self.new_content):
                f.write(ele)
        print('Successful')


if __name__ == '__main__':
    file_1 = 'sample_py_prog.txt'
    file_2 = 'output_1.txt'
    rc = RemoveComments(file_1, file_2)
    print(rc.show_content())
    print(rc.read_file())
    rc.write_new_file()
