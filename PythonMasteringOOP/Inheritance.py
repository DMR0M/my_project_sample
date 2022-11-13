class Employee:
    def __init__(self, name, title, rate_per_hr=None):
        self.name = name
        self.title = title
        if rate_per_hr is not None:
            rate_per_hr = float(rate_per_hr)
        self.rph = rate_per_hr

    def __str__(self):
        return f'Employee Description for {self.name}'

    def get_name(self):
        return self.name

    def get_title(self):
        return self.title

    def pay_per_yr(self):
        pay = 52 * 5 * 8 * self.rph
        return pay


class Manager(Employee):
    def __init__(self, name, title, salary, reports_list=None):
        self.salary = float(salary)
        if reports_list is None:
            reports_list = []
        self.reports_list = reports_list
        super().__init__(name, title)

    def get_reports(self):
        return self.reports_list

    def pay_per_yr(self, give_bonus=False):
        pay = self.salary
        if give_bonus:
            pay = pay + (.1 * self.salary)
            print(f'{self.name} gets a bonus for work')
        return pay


if __name__ == '__main__':
    e = Employee('RR', 'Software Engineer', 2.2)
    print(e)
    print(e.get_name())
    print(e.get_title())
    print(e.pay_per_yr())
    m = Manager('Rommel', 'Senior Software Engineer', 500)
    print(m.pay_per_yr(True))

