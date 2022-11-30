import sys


class Primes:
    """Class to determine if initialized int value is prime or not"""
    def __init__(self, n: int):
        self.num = n
        self.num_list = (n for n in range(1, self.num+1))  # Generator range list
        self.num_factors = 0
        self.factors = []
        self.range = 10000
        self.one_to_million = (n for n in range(1, self.range))

    def __repr__(self):
        one_mil = list(filter(Primes.prime_filter, self.one_to_million))
        primes_one_mil = (x for x in one_mil)
        return f'Prime Numbers 1 to 1 Million:\n{primes_one_mil}'

    @staticmethod
    def prime_filter(n) -> bool:
        n_list = (i for i in range(1, n+1))
        factors = 0
        for i, ele in enumerate(n_list):
            if n % ele == 0:
                factors += 1
        prime = True if factors <= 2 else False
        return prime

    def primes(self) -> bool:
        for i, ele in enumerate(self.num_list, start=1):
            if self.num % ele == 0:
                self.num_factors += 1
                self.factors.append(ele)

        print(f'\nFactors: {self.factors}'
              f'\nNumber of factors: {self.num_factors}')
        is_prime = True if self.num_factors <= 2 else False
        return is_prime


if __name__ == '__main__':
    # num = int(input('Type number to determine: '))
    p = Primes(200)
    print(p)
    # print(sys.getsizeof(p.num_list))
    # print(p.primes())


    