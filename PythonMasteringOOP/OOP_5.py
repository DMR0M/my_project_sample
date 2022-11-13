# class Employee:
#     """Using getters and setters"""
#     def __init__(self, name):
#         self.name = name
#         self.__salary = 0
#
#     @property
#     def get_salary(self):
#         return self.__salary
#
#     @get_salary.setter
#     def set_salary(self, salary):
#         self.__salary = salary
#
#     @get_salary.deleter
#     def del_salary(self):
#         del self.__salary

class Student:
    def __init__(self):
        self.__name = ' '
        self.__grade = 0

    @property
    def grade(self):
        return self.__grade

    @property
    def name(self):
        return self.__name

    @grade.setter
    def grade(self, new_grade):
        try:
            new_grade = int(new_grade)
        except (TypeError, ValueError) as e:
            raise type(e)(f'New grade: {str(new_grade)} is an invalid type' )
        if (new_grade < 0) or (new_grade > 100):
            raise ValueError(f'New grade: {str(new_grade)} must be between 0 and 100')
        self.__grade = new_grade

    @name.setter
    def set_name(self, s_name):
        self.__name = s_name


class Location:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def loc(self):
        return [self.x, self.y]

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def __repr__(self):
        return f'{type(self).__name__} (x: {self.x}) (y: {self.y})'


if __name__ == '__main__':
    # student_1 = Student('Rommel')
    # student_1.grade = 100
    # student_1.set_name = 'RR'
    # print(f'{student_1.name}: {student_1.grade}')
    loc = Location()
    loc.move_left()
    loc.move_left()
    loc.move_down()
    print(f'{loc.x}, {loc.y}')
    print(loc)
    loc.move_down()
    loc.move_down()
    loc.move_right()
    loc.move_down()
    loc.move_left()
    loc.move_left()
    print(loc.loc)









