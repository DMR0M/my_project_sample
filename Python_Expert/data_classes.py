from dataclasses import dataclass
import pandas as pd


@dataclass
class Students:
    first_name: str
    last_name: str
    age: int
    subjects: list[str]
    grades: list[int]

    def __repr__(self):
        gpa: float = sum(self.grades) / len(self.grades)
        return f'GPA: {gpa}'


if __name__ == '__main__':
    f_name = input('First Name: ')
    l_name = input('Last Name: ')
    age = int(input('Age: '))
    subj = [input('Type subjects: ') for i in range(6)]
    grd = [int(input(f'Grade for {sub}: ')) for sub in subj]
    
    std_1 = Students(f_name, l_name, age, subj, grd)
    print(std_1)
