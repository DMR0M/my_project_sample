class Animal:
    def __init__(self, name, classes):
        self.animal_class = classes
        self.animal_name = name

    def introduce(self):
        return f'Hi I am {self.animal_name}, and I am a {self.animal_class}'


class Dog(Animal):
    def __init__(self, name):
        super().__init__(self, name)

    def bark(self):
        return f"woof woof!"


my_animal_1 = Animal('RR', 'Mammal')
print(my_animal_1.introduce())
my_animal_2 = Dog('Douglass')
print(my_animal_2.introduce())
print(my_animal_2.bark())

