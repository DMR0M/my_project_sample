import sys


class Primes:
    """Class to determine if initialized int value is prime or not"""
    def __init__(self, n: int):
        self.num = n
        self.num_list = (n for n in range(1, self.num+1))  # Generator range list
        self.num_factors = 0
        self.factors = []

    def primes(self) -> bool:
        for i, ele in enumerate(self.num_list, start=1):
            if self.num % ele == 0:
                self.num_factors += 1
                self.factors.append(ele)
                
        print(f'\nFactors: {self.factors}' \
              f'\nnumber of factors: {self.num_factors}')
        is_prime = True if self.num_factors <= 2 else False
        return is_prime


if __name__ == '__main__':
    num = int(input('Type number to determine: '))
    p = Primes(num)
    print(sys.getsizeof(p.num_list))
    print(p.primes())
    