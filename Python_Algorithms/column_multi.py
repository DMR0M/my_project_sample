
class Multi:
    def __init__(self, x: list[int], y: list[int]):
        self.x = x
        self.y = y
        self.ans_list: list = []
        # [2, 5, 2]
        # [3, 2, 4]
        # [8+2, 8+3, 2]
        #

    def col_multi(self) -> int or str:
        one_nine = [i for i in range(0, 10)]
        last_num = 0
        # print(last)
        for j, ele_y in enumerate(self.y):
            for i, ele_x in enumerate(self.x):
                if ele_x and ele_y in one_nine:
                    ans = ele_x * ele_y
                    if ans > 9:
                        cherries = list(divmod(ans, 10))
                        cherry = cherries[0]
                        self.ans_list[i-1] += cherry
                        self.ans_list.append(cherries[1])
                        last_num = self.ans_list[0]
                    else:
                        self.ans_list.append(ans)
                else:
                    return f'Invalid Number Vectors:\n' \
                           f'{self.x}\n' \
                           f'{self.y}\n'
        if last_num > 9:
            vals = list(divmod(last_num, 10))
            self.ans_list.remove(last_num)
            a = vals[0]
            b = vals[1]
            self.ans_list.insert(0, b)
            self.ans_list.insert(0, a)
            # print(vals)
        print(last_num)
        return self.ans_list


if __name__ == '__main__':
    # print(list(divmod(10, 10)))
    vec_x = [2, 7, 1]
    vec_y = [5]
    m = Multi(vec_x, vec_y)
    print(m.col_multi())
