import math


class BinarySearch:
    """Class that searches for a number in a given list"""
    def __init__(self, sequence: list[int], target_num: int):
        self.seq = list(sorted(sequence))
        self.target = target_num
        self.sample_seq = [n for n in range(1, 10+1)]

    def binary_search(self):
        start_point = 0
        end_point = len(self.seq) - 1

        while start_point <= end_point:
            midpoint = start_point + math.floor((end_point-start_point)/2)
            mid_val = self.seq[midpoint]
            if self.target == mid_val:
                return f'Found item at index: {midpoint}'
            elif self.target < mid_val:
                end_point = midpoint - 1
            elif self.target > mid_val:
                start_point = midpoint + 1
            else:
                return None


if __name__ == '__main__':
    num_len = 5
    sample = [n for n in range(1, 101)]
    # num_lib = [int(input(f'Type number at index {n}: ')) for n in range(num_len)]
    find_item = int(input('Type number to find: '))

    bs = BinarySearch(sample, find_item)
    print(bs.seq)
    print(bs.binary_search())
