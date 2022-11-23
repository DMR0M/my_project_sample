from Display_Table import Table
import datetime as dt


if __name__ == '__main__':
    date_hired_1 = dt.datetime(2022, 5, 28)
    date_hired_2 = dt.datetime(2022, 5, 13)
    e1 = Table('RR', 'DM', 'Arellano', date_hired_1,
               16000)
    e2 = Table('Mari', 'Gamay', 'Arellano', date_hired_2,
               25000)
    e3 = Table('Pol', 'Perez', 'JRU', date_hired_1,
               25000)
    e4 = Table('Kirstin', 'Lu', 'JRU', date_hired_2,
               25000)
    e5 = Table('Joko', 'Diaz', 'GTHS', date_hired_2,
               27000)
    e1.store()
    e2.store()
    e3.store()
    e4.store()
    e5.store()
    e1.change = 'Rommel'
    print(e1.display_data())
    print(e1.write_csv())
