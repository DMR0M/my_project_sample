class Numbers:
    obj_count = 0   # static class variable

    def __init__(self, x, y, z):
        self.x_val = x
        self.y_val = y
        self.z_val = z
        self.xyz = []
        self.obj_list = []

    # returns a string representation of an object
    def __repr__(self):
        Numbers.obj_count += 1
        return f'Object {Numbers.obj_count} with {self.xyz} values'

    @property
    def get_xyz(self):
        self.xyz = [self.x_val ** 2, self.y_val ** 2, self.z_val ** 2]
        return self.xyz

    def __eq__(self, other):
        if not isinstance(other, Numbers):
            raise TypeError('Object was not an instance of Numbers')
        if self.xyz == other.xyz:
            return f'It is {True}'
        else:
            return f'It is {False}'

    def __add__(self, other):
        return self.x_val + self.y_val + self.z_val


if __name__ == '__main__':
    nums_1 = Numbers(5, 6, 7)
    print(nums_1.get_xyz)
    print(nums_1)
    nums_2 = Numbers(3, 17, 8)
    print(nums_2.get_xyz)
    print(nums_2)
    print(nums_1 == nums_2)
    print(nums_1 + nums_2)