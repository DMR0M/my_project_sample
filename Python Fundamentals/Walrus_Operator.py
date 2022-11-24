import math


class Grades:
    def __init__(self, grades: list[int]):
        self.g_list = grades
        self.Aplus = [n for n in range(95, 101)]
        self.A = [n for n in range(90, 95)]
        self.B = [n for n in range(76, 90)]
        self.marks: list[str] = ['EXCELLENT', 'GREAT', 'GOOD', 'FAILED']

    def get_average(self) -> float:
        gwa = (sum(self.g_list)) / len(self.g_list)
        return gwa

    def evaluate_grades(self) -> list:
        evaluation = []
        for i, ele in enumerate(self.g_list):
            if ele in self.Aplus:
                evaluation.append(self.marks[0])
            elif ele in self.A:
                evaluation.append(self.marks[1])
            elif ele in self.B:
                evaluation.append(self.marks[2])
            else:
                evaluation.append(self.marks[3])
        return evaluation

    def determine_honor(self) -> str:
        if self.marks[0] in (eval_list := self.evaluate_grades()):
            return f'{eval_list} contains 1 EXCELLENT and is with Honors'
        else:
            return f'{eval_list} contains no EXCELLENT and is NOT with Honors'


if __name__ == '__main__':
    s_grades = [95, 89, 93, 92, 90, 87, 86, 91]
    x_grades = [96, 97, 93, 92, 94, 93, 96, 98]
    g1 = Grades(s_grades)
    g2 = Grades(x_grades)
    # print(g2.get_average())

    if math.ceil((ave := g2.get_average())) >= 95:
        print(f'General Weighted Average:\n{(a := g2.get_average())}\n'
              f'You are a VALEDICTORIAN')
    elif math.ceil(ave := g2.get_average()) < 95 and (ave > 89):
        print(f'General Weighted Average:\n{(a := g2.get_average())}\n'
              f'You are a SALUTATORIAN')
    else:
        print('No honors')
