def main():
    my_dict = {'RR': 20, 'Rommel': 23, 'Rudolf': 25}
    # print(*my_dict.keys())
    # print(*my_dict.values())
    # print(my_dict)
    number_of_occurrences()
    print(*my_dict.items())


# 1. APPENDING A DICTIONARY
def appending_dictionary():

    # Using a list with equals value to signify key-value pairs
    my_config = {'logging': False, 'max-size': 1000, 'width': 500, 'height': 400, 'contrast': 50}
    print(f'This is the initial dictionary: \n{my_config}')

    # Define dictionary then create a list proceeding the dictionary variable with an equivalent value
    my_config['date_time'] = True
    my_config['dimensions'] = 3

    # Unpacking each values of the dictionary assigning each value to a variable from
    # first to last respectively
    a, b, c, d, e = my_config.values()
    print(f'This is the modified dictionary: \n{my_config}')

    # storing the values of the dictionary in a separate list using * args
    values_list = [*my_config.values()]
    print(values_list)


# 2. DELETING A PAIR IN A DICTIONARY
def deleting_pairs():

    flights = {'HK': 'JP', 'MNL': 'SG', 'UK': 'ID'}
    f_a, f_b, f_c = flights
    print(f"Available Flights: \n{f_a} --> {flights['HK']}, {f_b} --> {flights['MNL']}, "
    f"{f_c} --> {flights['UK']}")
    print(f"{f_a} --> {flights['HK']} is delayed for now")
    # del dictionary function
    del flights['HK']
    print(f"Available Flights right now: \n{f_b} --> {flights['MNL']}, {f_c} --> {flights['UK']}")

    print(f'Origins: {flights.keys()}')
    print(f'Destinations: {flights.items()}')

# EXERCISE A:
# Alien Tracking

# Given 3 aliens in n number - position with 3 diff speeds SLOW=3, MEDIUM=7, FAST=10.5
# and a target destination - x number, check the appropriate speed to determine the
# exact alien that can go in that exact x number.


def alien_tracking():
    # Goal is to find the alien(s) that can go to the destination without any remainder

    # Initialize given variables
    destination = float(input('Type a distance: '))
    location = 0
    slow = 3
    medium = 7
    fast = 10.5

    # Create a dictionary that contains each of the aliens attributes and set the exact alien to
    # false for each alien
    alien_1 = {'Position': location, 'Destination': destination, 'Speed': slow, 'Exact Alien': False}
    alien_2 = {'Position': location, 'Destination': destination, 'Speed': medium, 'Exact Alien': False}
    alien_3 = {'Position': location, 'Destination': destination, 'Speed': fast, 'Exact Alien': False}

    # Check each alien if their speed matches the destination with no remainders based on their position
    if destination % alien_1['Speed'] == alien_1['Position']:
        alien_1['Exact Alien'] = True

    if destination % alien_2['Speed'] == alien_2['Position']:
        alien_2['Exact Alien'] = True

    if destination % alien_3['Speed'] == alien_3['Position']:
        alien_3['Exact Alien'] = True

    # Print the exact alien(s) that can go to the destination without remainders
    print(f"{alien_1['Exact Alien']}, {alien_2['Exact Alien']}, {alien_2['Exact Alien']}")



def number_of_occurrences():
    # determines the vowels of each character of a given string
    quote = 'The quick brown fox jumps over the lazy dog'
    vowels = {v for v in quote if v in 'aeiou'}
    print(vowels)

    # determines the number of occurrence of vowels in the quote
    occu_vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    print(quote)
    for i in range(len(quote)):
        occu_vowels['a'] += 1 if quote[i] in 'a' else 0
        occu_vowels['e'] += 1 if quote[i] in 'e' else 0
        occu_vowels['i'] += 1 if quote[i] in 'i' else 0
        occu_vowels['o'] += 1 if quote[i] in 'o' else 0
        occu_vowels['u'] += 1 if quote[i] in 'u' else 0
    print(f"a = {occu_vowels['a']} | e = {occu_vowels['e']} | i = {occu_vowels['i']} | "
          f"o = {occu_vowels['o']} | u = {occu_vowels['u']}")


# Default Dictionaries
from collections import defaultdict
def default_dict():
    count = defaultdict(lambda: 0)
    numbers = [1, 1, 2, 3, 5, 8]
    for key in numbers:
        count[key] += 1
    print(count)

    # set default to set a default value of a key with no value
    d = {}
    d.setdefault('list', []).append(0)
    print(d)


if __name__ == '__main__':
    deleting_pairs()

