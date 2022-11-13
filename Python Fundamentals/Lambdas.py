def using_lambdas():
    # define a lambda by specifying a parameter or return type and the expression
    num_expr = lambda x: x ** x

    return num_expr(4)


class Numbers:
    def __init__(self, num_1, num_2, num_list):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_list = num_list

    def filter_list(self):
        filtered_list = filter(lambda i: i > self.num_2 + self.num_1, self.num_list)
        return list(filtered_list)


print(using_lambdas())
numbers = Numbers(5, 2, [12, 3, 17, 8, 2])
print(numbers.filter_list())
