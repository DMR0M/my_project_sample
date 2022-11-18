from functools import reduce


class Honors:
    """A class that evaluates a list if the GPA element is more than 90"""
    def __init__(self, gpa_list):
        self.gpa_list = gpa_list
        self.x = 10

    def eval_honors(self):
        honors_list = map(lambda x: x >= 90, self.gpa_list)
        return list(honors_list)

    def show(self):
        for i, ele in enumerate(self.gpa_list):
            print(f'GPA {i+1}: {ele}')

    def get_total_ave_of_gpa(self):
        total_ave1 = sum(self.gpa_list)/len(self.gpa_list)
        return '%.2f' % total_ave1

        # total_ave = reduce(lambda x, y: (x+y)/len(self.gpa_dict), self.gpa_dict)
        # return total_ave

    def get_max(self):
        return max(self.gpa_list)

    def get_product(self):
        return reduce(lambda x, y: x * y, self.gpa_list)
        # return list(self.gpa_list)


class Names:
    def __init__(self, names_list):
        self.names_list = names_list

    def get_length_each(self):
        length_each = map(lambda x: len(x), self.names_list)
        return list(length_each)

    def filter_names(self):
        filtered_list = filter(lambda x: len(x) < 6, self.names_list)
        return list(filtered_list)

    def get_reverse(self):
        for i, ele in enumerate(self.names_list):
            print(f'{i+1}: {ele[::-1].lower()}')

        for i, ele in enumerate(self.names_list[::-1]):
            print(f'{ele}', end=' ')
        # reversed_names = map(lambda x: x[::-1], self.names_list)
        # return list(reversed_names)


class Products:
    def __init__(self, num_dict):
        self.num_dict = num_dict
        self.name_age_dict = {'RR': 23, 'Rosano': 31, 'James': 29, 'Honey': 25,
                              'Rudy': 63, 'Trisha': 11, 'Rojean': 18, 'Paciano': 26}

    def sort_by_product(self):
        sorted_dict = sorted(self.num_dict.sort(key=lambda x: x[1] * x[0]))
        return sorted_dict

    def print_val(self):
        sorted_dict = sorted(self.name_age_dict.items(), key=lambda i: i[1], reverse=True)
        return sorted_dict


class GetPrime:
    def __init__(self, num):
        self.num = num
        self.nums_list = [n for n in range(1, self.num+1)]
        self.multiples = 0
        self.mult_list = []
        self.one_hundred_list = [n for n in range(101)]

    def __repr__(self):
        return f'Getting Prime Numbers'

    def get_prime(self) -> bool:
        for i, ele in enumerate(self.nums_list[::-1]):
            if self.num % ele == 0:
                self.multiples += 1
                self.mult_list.append(ele)
        # prints the multiples of the given number
        print(f'Factors: {self.mult_list}')
        if self.multiples > 2:
            return True
        return False

    @staticmethod
    def get_prime_c(n) -> bool:
        nums_list = [n for n in range(1, n + 1)]
        factors = 0
        for i, ele in enumerate(nums_list[::-1]):
            if n % ele == 0:
                factors += 1
        if factors > 2:
            return True
        return False

    def filter_nums(self):
        filtered_n_list = filter(GetPrime.get_prime_c, self.one_hundred_list)
        return list(filtered_n_list)


if __name__ == '__main__':
    n_list = [n for n in range(101)]
    check_num = int(input('Enter number to determine: '))
    gp = GetPrime(check_num)
    print(gp)

    # prints if the given number is prime or not
    is_prime = gp.get_prime()
    print(is_prime)

    # prints the prime numbers from 1-100
    print(gp.filter_nums())

    # def get_prime(n) -> bool:
    #     nums_list = [n for n in range(1, n+1)]
    #     factors = 0
    #     for i, ele in enumerate(nums_list[::-1]):
    #         if n % ele == 0:
    #             factors += 1
    #     if factors > 2:
    #         return True
    #     return False



    # student_gpa_list = [91, 90, 87, 93, 96, 95, 86]
    # honors = Honors(student_gpa_list)
    #
    # r_list = [5, 17, 8, 3, 13, 23, 6]
    # honors1 = Honors(r_list)

    # honors.show()
    # print(honors.eval_honors())
    # print(honors.get_total_ave_of_gpa())
    # print(honors.get_max())
    # print(honors1.get_product())
    # honors.gpa_list.insert(0, 95)
    # print(honors.gpa_list)

    # names = ['RR', 'Joko', 'Shane', 'Jolina', 'Rojean', 'Jean', 'Honey', 'Rosano']
    # obj1 = Names(names)
    # print(obj1.get_length_each())
    # print(obj1.filter_names())
    # obj1.get_reverse()

    # numbers_dict = {1: 4, -8: 17, 3: -5, -6: -3, -9: 7, 6: 2, 10: -5}
    # product = Products(numbers_dict)
    # print(product.print_val())


