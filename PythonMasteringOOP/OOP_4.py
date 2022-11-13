
class Salary:
    def __init__(self, pay_amount, bonus_pay):
        self.pay_amount = pay_amount
        self.bonus_pay = bonus_pay
        self.income_tax = .08

    def calc_fortnightly_salary(self):
        net_salary = (self.pay_amount + self.bonus_pay) * (1 - self.income_tax)
        return net_salary


class Employee:
    def __init__(self, id_number, name, contact_num, pay, bonus):
        self.id = id_number
        self.name = name
        self.contact = contact_num
        self.pay = pay
        self.bonus = bonus

        # Object Composition (Instantiating a class to another class' method)
        self.salary = Salary(pay, bonus)

    def total_salary(self):
        print(f'\nTotal Salary is: {self.salary.calc_fortnightly_salary()}\n')

    # def show(self):
    #     print(f'\nEmployee ID: {self.id}\n'
    #           f'Employee Name: {self.name}\n'
    #           f'Employee Contact Number: {self.contact}\n'
    #           f'Employee Initial Pay: {self.pay}\n'
    #           f'Employee Bonus Pay: {self.bonus}\n')


class Grades:
    def __init__(self, grade):
        self.subjects = ['Filipino', 'Math', 'Science', 'English',
                         'Social Studies', 'Literature']
        self.grade = grade

    # Implement using two iteration for loop for two lists using zip func
    def grades_eval(self):
        # Method that evaluates the given grades if it is PASSED or FAILED
        for ele_x, ele_y in zip(self.grade, self.subjects):
            if ele_x >= 75:
                print(f'{ele_y}\n\t{ele_x} : PASSED\n')
            else:
                print(f'{ele_y}\n\t{ele_x} : FAILED\n')

    def get_average(self):
        sum_of_grades = sum(self.grade)
        average = sum_of_grades/len(self.grade)
        return '%.2f' % average


class Student:
    def __init__(self, student_id_num, student_name, grades):
        self.student_id_num = student_id_num
        self.student_name = student_name
        self.obj_grades = grades

    def eval_student_grades(self):
        self.obj_grades.grades_eval()

    def get_student_average(self):
        print(f'ID: {self.student_id_num}\n'
              f'Name: {self.student_name}\n'
              f'Total grade average: ')
        return self.obj_grades.get_average()


if __name__ == '__main__':
    # User input student id and name
    print("*** ENTER STUDENT'S INFO ***\n")
    s_id = int(input('Enter student id number: '))
    s_name = input('Enter student name: ')

    # User input grades for the 6 subjects
    subjects = ['Filipino', 'Math', 'Science', 'English', 'Social Studies', 'Literature']
    grades_list = []
    try:
        print("\n*** ENTER STUDENT'S GRADES ***\n")
        for i, ele in enumerate(subjects):
            grade_input = int(input(f'Input your grade in {ele}: '))
            grades_list.append(grade_input)
    except ValueError:
        print('Invalid input for subject grade ')
        exit()

    grades_1 = Grades(grades_list)

    # Aggregation is applied, passing an instance of a class
    # as argument to another instance of a different class

    student_1 = Student(s_id, s_name, grades_1)
    print('\n*** STUDENT GRADE EVALUATION ***\n')
    student_1.eval_student_grades()
    print('\n*** STUDENT GRADE POINT AVERAGE ***\n')
    print(student_1.get_student_average())

    # em_id = input('Enter Employee ID: ')
    # em_name = input('Enter Name: ')
    # em_contact = int(input('Enter Contact Number: '))
    # em_init_pay = float(input('Enter Initial Pay: '))
    # em_bonus_pay = float(input('Enter Bonus Pay: '))
    # emp1 = Employee(em_id, em_name, em_contact, em_init_pay, em_bonus_pay)
    # emp1.total_salary()



