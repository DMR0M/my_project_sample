class DayNames:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None


if __name__ == '__main__':
    e1 = DayNames('Mon')
    e2 = DayNames('Tue')
    e3 = DayNames('Wed')
    e4 = DayNames('Thu')
    e5 = DayNames('Fri')
    e6 = DayNames('Sat')
    e7 = DayNames('Sun')

    e1.next_val = e2
    e2.next_val = e3
    e3.next_val = e4
    e4.next_val = e5
    e5.next_val = e6
    e6.next_val = e7
    e7.next_val = e1
    print(e1.next_val)
