from dataclasses import dataclass, field


@dataclass()
class MultiCalc:
    calc: str

    def __repr__(self):
        return f'Equation: {self.calc}'

    def multi_calc(self) -> float or str:
        equation = self.calc.split(' ')
        operation = ['+', '-', '*', '/']
        op_list = list(filter(lambda x: x if x in operation else 0, equation))
        nums_list = list(filter(lambda x: x if x not in operation else 0, equation))
        nums_list = list(map(float, nums_list))
        ans = nums_list.pop(0)

        # Operations
        for i, num in enumerate(nums_list):
            if op_list[i] == '+':
                ans += num
            elif op_list[i] == '-':
                ans -= num
            elif op_list[i] == '*':
                ans *= num
            elif op_list[i] == '/':
                ans /= num
            else:
                return 'Invalid operation'
        return f'{"%.2f" % ans}'


if __name__ == '__main__':
    calculation = input('Type calculation: ')
    c = MultiCalc(calculation)
    print(c)
    print(c.multi_calc())
