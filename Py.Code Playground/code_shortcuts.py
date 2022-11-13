# Shortcuts in Python

# 1: Print using F strings
def print_function(name, age):
    # shortcut to print a line and store as variable
    line = F'Hello {name} you are {age}-years old'
    print(line)
    # shortcut to print and not use concatenation
    print(f'Hello {name} your are {age}-years old')


# 2: Unpacking or assigning individual variables from the indices of a data structure
def unpacking_function():
    my_tup = (2,4,6,8,10,12)
    my_list = [1,3,5,7,9,11]
    my_dict = {"a": 0.5, "b": 1.5, "c": 2.5}
    string = 'learner'
    # Assign each index a variable
    a, b, c, d, e, f = my_tup
    g, h, i, j, k, l = my_list
    m, n, o = my_dict
    p, q, r, s, t, u, v = string


# 3: Comprehensions a way to initialize and create a data collection with loops and conditions in 1 line
def comprehension_function():
    # 1 line loop with condition inside a data structure type
    # prints all the even numbers from 0 to 100
    list_com = [i for i in range(100) if i % 2 == 0]
    print(list_com)
    sentence = 'This is my sentence'
    char_list_sentence = {char: sentence.count(char) for char in list(sentence)}
    print(char_list_sentence)


# 4: Object Multiplication multiply a variable
def obj_multiplication():
    # Multiply a string
    obj = 'RR' * 5
    print(obj)

    # Multiply a list
    int_list = [2, 4, 5] * 5
    print(int_list)


# 5: Ternary Conditions or 1 line condition statement
def ternary_con(number):
    value = True if number % 3 == 0 else False     # Inline/Ternary Condition
    # assign a value to a variable to check if condition is met
    # else if condition is not met assign otherwise
    print(value)


# 6: Zip Functions it is used to combine a data structure type
def zip_function():
    names = ['RR', 'Joko', 'Rudy', 'R']
    ages = [23, 24, 62]
    eye_color = ['Green', 'Blue', 'Brown']

    print(list(zip(names, ages, eye_color)))


# 7: *args and **kwargs used to pass multiple variables to a function
def create_list():
    list = ['a', 'b', 'c', 'd']
    dictionary = {'x': 1, 'y': 2, 'z': 3}


    # print_values(*args/**kwargs )


def print_values(values):
    for i in range(len(values)):
        print(f'the value of index[{i}] is {values[i]} \n')
        break

zip_function()
exit()