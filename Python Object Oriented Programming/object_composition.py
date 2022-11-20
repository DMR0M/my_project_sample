class Salary:
    def __init__(self, salary, bonus=0):
        self.salary = salary
        self.bonus = bonus

    def show_annual_salary(self):
        return (self.salary * 12) + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self._name = name
        self.age = age
        # Object Composition
        self.emp_salary = Salary(pay, bonus)

    def __repr__(self):
        return f'You are {self._name}.'

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def get_name(self, new_name):
        self._name = new_name

    def total_salary(self):
        return self.emp_salary.show_annual_salary()


if __name__ == '__main__':
    e1 = Employee('RR', 23, 16500, 12770.93)
    # print(e1.total_salary())
    # print(e1.get_name())

    print(e1.get_name)
    e1.get_name = 'Rommel'
    print(e1.get_name)

    print(e1)

    e2 = Employee('Jasmine', 22, 17000, 13156.96)

