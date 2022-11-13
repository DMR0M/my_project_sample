# Class names must begin with an uppercase letter
class Users:
    def __init__(self, name, age, id_num, contact, address):
        # assign self to the parameters of the __init__ method to represent as class variables for the methods
        self.name = name
        self.age = age
        self.id_num = id_num
        self.contact = contact
        self.address = address

    def permission(self, age):
        print(f'{age} given age\nACCESS GRANTED')

    def age_verification(self, age):
        print('ACCESS DENIED') if age < 18 else self.permission(age)


# Instantiate an object
# user_1 = Users('RR', 17, 19023, 9079090310, 'Pasig City')
# user_1.age_verification(18)
# print('\n')


class Cars:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

    def get_car_description(self):
        car_desc = f'{self.year} {self.manufacturer} {self.model}'
        return car_desc


# car_1 = Cars('Ford', 'Territory', 2019)
# car_2 = Cars('Honda', 'City', 2021)
# print(car_1.get_car_description())
# print(car_2.get_car_description())


# Inheritance

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'Hi there I am a {self.name} and I am {self.age}')

    def speak(self):
        print("I don't know what to say")


class Bird(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('chirp')

    def introduce(self):
        print(f'Hi there I am a {self.name}, I am {self.age} and I am {self.color}')


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('meow')

    def introduce(self):
        print(f'Hi there I am a {self.name}, I am {self.age} and I am {self.color}')


# Instances

# p = Pet('Tim', 19)
# p.speak()
# c = Cat('Roger', 4, 'Yellow')
# c.introduce()
# d = Bird('Heaven', 2, 'Green')
# d.introduce()


class Person:
    number_of_people = 0

    def __init__(self, name, age, location, position):
        # Determine how many instances that are created of super class Person
        Person.add_person()
        self.name = name
        self.age = age
        self.location = location
        self.position = position

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    def make_coffee(self):
        print('I am making coffee')

    def work_overtime(self):
        print('I can work overtime')

    def introduce(self):
        print(f"Hi there my name's {self.name}, I am {self.age} years old and I am from {self.location}")


class Managers(Person):
    number_of_managers = 0

    def __init__(self, name, age, location, position, mastery):
        super().__init__(name, age, location, position)
        Managers.number_of_managers += 1
        self.mastery = mastery

    def introduce(self):
        print(f'Hello my name is {self.name}, I am {self.age} and I mastered {self.mastery}')

    def make_coffee(self):
        print("Sorry I don't make coffee")

    def supervise(self):
        print('I supervise')


class Employees(Person):
    def __init__(self, name, age, location, position, training):
        super().__init__(name, age, location, position)
        self.training = training

    def introduce(self):
        print(f'Hello my name is {self.name}, I am {self.age} and I am training in {self.training}')

    def training(self):
        print(f'I train a lot in {self.training()}')


# Instances

employee1 = Employees('RR', 23, 'Pasig City', 'Trainee', 'Python')
employee1.introduce()
employee1.make_coffee()

manager1 = Managers('Chikoy', 29, 'Mandaluyong City', 'Engineering Manager', 'Java')
manager1.introduce()
manager1.supervise()
manager1.work_overtime()

e2 = Person('Rommel', 24, 'Pasig City', 'Trainee')
manager2 = Managers('Jerie', 33, 'Pasig City', 'Engineering Supervisor', 'C++')
manager2.introduce()

print(Person.number_of_people_())


