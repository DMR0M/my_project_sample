from electric_car import ElectricCar as ECar


class Car:
    """A simple Car class to represent car"""
    def __init__(self, make, model, year, battery_size):
        self.make = make
        self.model = model
        self.year = year
        self.battery = battery_size

    def get_descriptive_name(self):
        print(f'Make: {self.make}\nModel: {self.model}'
              f'\nYear: {self.year}')


if __name__ == '__main__':
    # car_1 = Car('Ford', 'Territory', 2019, 105)
    # car_1.get_descriptive_name()

    electric_car_1 = ECar('Tesla', 'Model X')
    electric_car_1.get_range()
    electric_car_1.upgrade_battery()
    electric_car_1.get_range()



