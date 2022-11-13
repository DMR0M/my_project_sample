class Battery:
    def __init__(self):
        self.capacity = 1555


class ElectricCar(Battery):
    def __init__(self, make: str, name: str):
        super().__init__()
        self.brand = make
        self.car_name = name

    def upgrade_battery(self):
        if self.capacity <= 100:
            print('Upgrading Battery...')
            self.capacity = 100
        else:
            print('Battery Overload')
            self.capacity = 100

    def get_range(self):
        print(f'Make: {self.brand}\nBattery Capacity: {self.capacity}')