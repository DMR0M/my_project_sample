class Meta(type):
    def __new__(mcs, class_name, inherits, attributes):

        # Declare empty dictionary
        my_dict = {}

        for key, val in attributes.items():
            if key.startswith('s'):
                my_dict[key] = val
            else:
                my_dict[key.upper()] = val

        return type(class_name, inherits, my_dict)


class Person(metaclass=Meta):
    a = 10
    b = 20

    def add_attrs(self):
        c = Person.a + Person.b
        print(c)


person_1 = Person()

