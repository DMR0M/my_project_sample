class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width


class Square(Rectangle):
    def __init__(self, height, width):
        # Super - used to access the methods of the parent class
        super().__init__(height, width)

    def area(self):
        return self.height*self.width


class Cube(Rectangle):
    def __init__(self, height, width, length):
        super().__init__(height, width)
        self.length = length

    def volume(self):
        return self.height*self.width*self.length


class Employee:
    """A business organization class hierarchy
       through inheritance implementation"""
    employee_count = 0

    def __init__(self, name, working_time, salary, promotion: bool):
        self.w_time = working_time
        self.salary = salary
        self.is_promoted = promotion
        self.name = name
        Employee.employee_count += 1
        self.e_count = Employee.employee_count

    def display_employee_status(self):
        return f'Name: {self.name}\n' \
               f'Number of worked hrs: {self.w_time}\n' \
               f'Salary: {self.salary}\n' \
               f'Promotion: {self.is_promoted}\n' \


    def display_total_employees(self):
        return self.e_count


class Manager(Employee):
    def __init__(self, m_working_time, m_salary, m_promotion,
                 m_name, subordinates: list):
        super().__init__(m_working_time, m_salary, m_promotion, m_name)
        self.subordinates = subordinates

    def display_subordinates(self):
        return self.subordinates


class Supervisor(Employee):
    def __init__(self, s_working_time, s_salary, s_promotion, supervise_time):
        super().__init__(None, s_working_time, s_salary, s_promotion)
        self.supervise_time = supervise_time


class Subordinates(Supervisor):
    def __init__(self, sub_working_time, sub_salary, sub_promotion,
                 tasks, nickname):
        super().__init__(sub_working_time, sub_salary, sub_promotion, None)
        self.tasks = tasks
        self.name = nickname

    def __str__(self):
        return self.name

    # Polymorphism
    def display_employee_status(self):
        return f'Name: {self.name} \n' \
               f'Number of worked hrs: {self.w_time}\n' \
               f'Salary: {self.salary}\n' \
               f'Promotion: {self.is_promoted}\n' \
               f'Number of Tasks: {len(self.tasks)}\n' \
               f'Tasks: {self.tasks}\n'


if __name__ == '__main__':

    # Function to compile objects into list
    def compile_objects(*args) -> list:
        return list(args)

    sub_1 = Subordinates(8.5, 36000, False, ['Coding', 'Testing'], 'RR')
    sub_2 = Subordinates(8, 45000, False, ['Coding', 'Review', 'Testing'], 'Chikoy')
    sub_3 = Subordinates(10, 40000, True, ['Coding', 'Review'], 'Kevin Roi')
    sub_4 = Manager('Cyrelle', 8, 50000, False, [sub_1, sub_2, sub_3])

    status_sub_1 = sub_1.display_employee_status()
    status_sub_2 = sub_2.display_employee_status()
    status_sub_3 = sub_3.display_employee_status()

    status_sub_4 = sub_4.display_employee_status()

    employees_list: list = compile_objects(status_sub_1, status_sub_2, status_sub_3)
    managers_list: list = compile_objects(status_sub_4)

    for i, ele in enumerate(employees_list):
        print(f'Employee List:\nID: {i+1}\nStatus:\n{ele}')

    for i, ele in enumerate(managers_list):
        print(f'Manager List:\nID: {i + 1}\nStatus:\n{ele}')

    # square = Square(3, 4)
    # cube = Cube(4, 4, 6)
    # print(square.area())
    # print(cube.volume())
