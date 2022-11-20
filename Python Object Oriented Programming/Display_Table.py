import pandas as pd
import datetime as dt


class Data:
    data_list = []

    def __init__(self, first_name, last_name, school,
                 hire_date, salary):
        self._first_name = first_name
        self._last_name = last_name
        self._school = school
        self._hire_date = hire_date
        self._salary = salary
        self._data = [self._first_name, self._last_name, self._school,
                      self._hire_date, self._salary]
        self.cols = ['First Name', 'Last Name', 'School',
                     'Hire Date', 'Salary']
        self.data_table = ''

    def store(self):
        Data.data_list.append(self._data)
        return Data.data_list

    @property
    def change(self):
        return self._data

    @change.setter
    def change(self, val):
        prompt = input('Change what value? \nf - first name\nl - last name\n')
        if prompt.lower() == 'f':
            self._data[0] = val
        elif prompt.lower() == 'l':
            self._data[1] = val
        else:
            print('Invalid Input')


class Table(Data):
    def show(self):
        return self._data

    def display_data(self):
        self.data_table = pd.DataFrame(Data.data_list, columns=self.cols)
        return self.data_table

    def write_csv(self):
        self.data_table = pd.DataFrame(Data.data_list, columns=self.cols)
        self.data_table.to_csv('../Files/data.csv')
        return 'Successful'


if __name__ == '__main__':
    data_hired_1 = dt.datetime(2022, 5, 28)
    data_hired_2 = dt.datetime(2022, 5, 13)
    e1 = Table('RR', 'DM', 'Arellano', data_hired_1,
               16000)
    e2 = Table('Mari', 'Gamay', 'Arellano', data_hired_2,
               25000)

    e1.change = 'Rommel'
    e1.store()
    e2.store()
    print(e1.display_data())
    e1.write_csv()





