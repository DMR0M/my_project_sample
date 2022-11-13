class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.message1 = 'This car has 100+ miles traveled'
        self.message2 = 'This car has not yet traveled far'

    def print(self):
        desc = f'{self.make} {self.model} {self.year}'
        print(desc)

    def read_odometer(self):
        print(f'This car has {self.odometer} miles on it')

    def update_odometer(self, mileage):
        self.odometer = mileage
        print(self.message1) if mileage >= 100 else print(self.message2)

    def increment_odometer(self, miles):
        self.odometer += miles
        self.increment_odometer(miles) if miles > 0 else print('Invalid added miles')


car1 = Car('Ford', 'Territory', 2019)
car2 = Car('Honda', 'City', 2022)

car1.print()
car1.update_odometer(87)
car1.read_odometer()

car2.print()

car2.update_odometer(12_500)
car2.read_odometer()

car2.increment_odometer(-100)
car2.read_odometer()


