def main():
    # cube_list = [cube(i) for i in range(1, 11)]
    # print(cube_list)
    get_info()


# 1: * args and ** kwargs
# A * used to pass all elements in a list and all keys in a dictionaries
def args_and_kwargs():
    my_list = [x for x in range(1, 11) if x % 2 == 0]
    passing_arguments(*my_list)


def passing_arguments(a, b, c, d, e):
    print(a + b + c + d + e)


def get_info():
    info = {'location': '', 'known for': ''}
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    location = input('Enter location: ')
    info['location'] = location
    skills = input('Person is known for: ')
    info['known for'] = skills

    print(keyword_arguments(first_name, last_name, l=location, s=skills))


# Passing a **kwargs or keyword arguments from a dictionary
def keyword_arguments(first, last, **info):
    # print first and last variable
    print(f"{first} {last}")
    # unpack values of info dictionary
    a, b = info.values()
    # create a new list to contain the unpacked values of the info dictionary
    info_list = [a, b]
    # return the new list
    return info_list


# Function to cube a given number
def cube(n):
    return n**3


if __name__ == '__main__':
    main()
