
class PrimeOrComposite:
    def __init__(self, n):
        self.n = n
        self.n_list = [n for n in range(1, self.n+1)]
        self.factors = 0
        self.factors_list = []

    def determine_if_prime(self) -> str:
        if self.n > 0:
            for i, ele in enumerate(self.n_list[::-1]):
                if self.n % ele == 0:
                    self.factors_list.append(ele)
                    self.factors += 1
            if self.factors > 2:
                return 'No'
            return 'Yes'
        else:
            print('0 and all negative integers are not prime or composite')


if __name__ == '__main__':
    num_input = int(input('Type the number to determine: '))
    obj_1 = PrimeOrComposite(num_input)
    print(f'Is it a prime number: {obj_1.determine_if_prime()}')
    print(f'Number of factors: {obj_1.factors}')
    print(f'Factors: {obj_1.factors_list}')
