from dataclasses import dataclass


@dataclass()
class MultiCalc:
    calc: str

    def __repr__(self):
        return f'Equation: {self.calc}'

    def multi_calc(self) -> float or str:
        equation = self.calc.split(' ')
        operations = ['+', '-', '*', '/', '^']

        # creating list containing arithmetics filtering main list input
        op_list = list(filter(lambda x: x if x in operations else 0, equation))

        # creating list containing only numbers as str filtering main list input
        nums_list = list(filter(lambda x: x if x not in operations else 0, equation))

        # converting elements nums_list to float
        nums_list = list(map(float, nums_list))

        # initializing var to first element in nums_list
        ans = nums_list.pop(0)

        # operations
        for i, num in enumerate(nums_list):
            if op_list[i] == '+':
                ans += num
            elif op_list[i] == '-':
                ans -= num
            elif op_list[i] == '*':
                ans *= num
            elif op_list[i] == '/':
                ans /= num
            elif op_list[i] == '^':
                ans **= num
            else:
                return 'Invalid operation'
        return f'{"%.2f" % ans}'


if __name__ == '__main__':
    calculation = input('Type calculation: ')
    c = MultiCalc(calculation)
    print(c)
    print(c.multi_calc())
