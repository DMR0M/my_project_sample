# Concat lists with strings with the .join() string method

my_string = ['Rommel', 'Rudolf', 'A.', 'Dela', 'Merced']
seperator = ' '
new_string = seperator.join(my_string)

name = 'Rommel'
print('Yeah!') if name in my_string else print('Nah!')

# Combine dictionaries with unique items using **

d1 = {'name': 'RR', 'age': 23, 'location': 'Pasig City', 'occupation': 'Software Programmer'}
d2 = {'name': 'Joko', 'age': 24, 'location': 'Makati City'}
merge = {**d1, **d2}
print(merge)
