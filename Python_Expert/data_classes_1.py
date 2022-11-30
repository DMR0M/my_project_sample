from dataclasses import dataclass, field


@dataclass()
class Employee:
    first_name: str
    last_name: str
    age: int
    salary: float
    total_work_hrs: float
    is_regular: bool

    def __hash__(self):
        pass

    @property
    def change_first_n(self) -> str:
        return f'Change name to {self.first_name}'

    @change_first_n.setter
    def change_first_n(self, new_f_name) -> None:
        self.first_name = new_f_name

    @property
    def change_last_n(self) -> str:
        return f'Change name to {self.first_name}'

    @change_last_n.setter
    def change_last_n(self, new_l_name) -> None:
        self.first_name = new_l_name

    def get_annual_salary(self) -> float:
        return self.salary * 12


if __name__ == '__main__':
    data_1 = ('RR', 'Dela Merced', 23, 16781.91, 800, False)
    data_2 = ('Joko', 'Diaz', 23, 22550.56, 1900, True)
    data_3 = ('Maricar', 'Gamay', 22, 18750.43, 1000, True) # NOQA

    emp_1 = Employee(*data_1)
    emp_2 = Employee(*data_2)
    emp_3 = Employee(*data_3)

    print(emp_1.get_annual_salary())
    print(emp_2.get_annual_salary())
    print(emp_3.get_annual_salary())

    change_n = input('Type first name: ')
    emp_1.change_first_n = change_n
    print(emp_1.first_name)
