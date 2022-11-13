import math
import pandas as pd


class RPM:
    """A class that performs Russian Peasant Multiplication Algorithm"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def perform_rpm(self) -> object:
        halving = [self.x]
        doubling = [self.y]

        while min(halving) > 1:
            halving.append(math.floor(min(halving)/2))

        while len(doubling) < len(halving):
            doubling.append(max(doubling) * 2)

        half_double_data = pd.DataFrame(zip(halving, doubling))  # Create a data frame
        half_double_data = half_double_data.loc[half_double_data[0] % 2 == 1]
        ans = sum(half_double_data.loc[:, 1])

        print(half_double_data)
        return ans

    def halve(self) -> float:
        lst = [2**0, 2**3, 2**4, 2**6]
        f_lst = map(lambda x: x, lst)
        print(list(f_lst))
        return self.x/2


if __name__ == '__main__':
    m = RPM(87, 10)
    m1 = RPM(18, 89)
    print(m.perform_rpm())
    print(m1.perform_rpm())
    # print(m.halve())

