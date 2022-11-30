# Creating a class named Dog
class Dog:
    # initialize class variables as parameters to __init__ method
    def __init__(self, name, age, color):
        # assign self to the parameters of the __init__ method to represent as class variables for the methods
        self.name = name
        self.age = age
        self.color = color

    def roll_over(self):
        print(f'{self.name} rolls over the floor')

    def bark(self):
        print(f'{self.name} barks at the guests')


# Object
my_dog = Dog('Patty', 3, 'Blue')
print(my_dog)




