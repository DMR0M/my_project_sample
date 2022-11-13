class Euclid:
    def euclid_algo(self, x, y):
        larger = max(x, y)
        smaller = min(x, y)

        remainder = larger % smaller

        if remainder == 0:
            return smaller
        if remainder != 0:
            return self.euclid_algo(smaller, remainder)


if __name__ == '__main__':
    nums = Euclid()
    print(nums.euclid_algo(17, 34))
