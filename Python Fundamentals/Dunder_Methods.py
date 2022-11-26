class Sample:
    """Dunder or Magic Methods in Python"""
    """Also known as Data Model Methods"""
    def __init__(self, start=10, end=100):
        self.s = start
        self.e = end
        self.lst = [(lambda x: x // 2)(x) for x in range(self.s, self.e)]
        self.hundred = [n for n in range(1, 100+1)]
        self.multiplier = 2
        self.new: float = 0

    # Used to override of printing the object
    def __repr__(self):
        return f'Total:\n{self.lst}'

    # Used to override comparing objects
    def __eq__(self, other) -> str and bool:
        if self.hundred == other:
            return f'Objects are equal'
        else:
            return False

    # Used to override multiplying objects
    def __mul__(self, other):
        self.new = other * self.multiplier


if __name__ == '__main__':
    s = Sample()
    # print(divs := s.lst)
    # print(s)
    nums = [i for i in range(1, 100+1)]
    num = 10
    print(s == nums)
    print(s * 3)
