# Insertion Function

def ins_func(lst: list[int], val: int) -> list[int]:
    # 1st parameter is an iterable integer object
    # 2nd parameter is an integer value
    # Function returns an iterable integer object
    ins_loc = 0
    for i, ele in enumerate(lst):
        if val > ele:
            ins_loc = i + 1
            break
    lst.insert(ins_loc, val)
    return lst


def ins_sort(lst: list[int]) -> list[int]:
    # parameter is an iterable integer object
    # Function returns a sorted iterable integer object
    new_lst = []
    while len(lst) > 0:
        to_ins = lst.pop(0)
        new_lst = ins_func(new_lst, to_ins)
        # print(f'{lst} : {new_lst}')
    return new_lst


if __name__ == '__main__':
    sample = [7, 5, 6, 1, 3]
    print(ins_sort(sample))

