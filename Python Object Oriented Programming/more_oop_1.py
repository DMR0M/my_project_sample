"""LESSONS ABOUT DATA CLASSES IN PYTHON"""

# For Python 3.10 above

# add (frozen) cannot change instances of objects
# add (kw_only) can only make argument instances with keywords
# add (match_args) supports match case similar
# in other languages' switch case statements
# add (slots)

# Data Classes in Python
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.digits, k=9))


@dataclass(kw_only=True)
class Person:
    name: str
    address: str
    age: int
    if_active: True
    id_num: str = field(init=False, default_factory=generate_id)
    search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.search_string = f'{self.if_active}'


def main():
    person_1 = Person(name='RR', age=23, address='Pasig City', if_active=True)
    person_2 = Person(name='Rommel', age=25, address='Laguna', if_active=False)
    person_3 = Person(name='Joko', age=24, address='Makati City', if_active=True)
    people: list = [person_1, person_2, person_3]
    # comprehension: list = [print(f'Person {i+1} - {person}')
    #                       for i, person in enumerate(people)]
    print('List of Active People: ')
    for i, person in enumerate(people):
        if person.__dict__['if_active']:
            print(f'Person {i+1} - {person.__dict__["name"]}')


if __name__ == '__main__':
    main()

