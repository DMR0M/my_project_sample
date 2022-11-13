"""Create a gui application that takes in user input coordinates
    and plots them in a graph and shows the graph with the given
    coordinates.
    NOTE: Implement OOP"""

import matplotlib.pyplot as plt


class CreateUserLineGraph:
    def __init__(self, x, y):
        self.x: list[int] = x
        self.y: list[int] = y

    def create_line_graph(self):
        plt.style.use('fivethirtyeight')
        flg, ax = plt.subplots()
        plt.title('User Created Line Graph: ')
        ax.plot(self.x, self.y)
        ax.scatter(self.x, self.y, s=100)
        plt.show()


if __name__ == '__main__':
    while ValueError:
        try:
            x_y_length = int(input('Type the length of x and y values: '))
            if x_y_length > 0:
                break
        except ValueError:
            print('Please only input numbers')


    def generate_x():
        x_values: list[int] = []
        for i in range(x_y_length):
            while ValueError:
                try:
                    ele = int(input(f'Input x value, number {i+1}: '))
                    x_values.append(ele)
                    break
                except ValueError:
                    print('Please only input numbers')

        return x_values

    def generate_y():
        y_values: list[int] = []
        for i in range(x_y_length):
            while ValueError:
                try:
                    ele = int(input(f'Input y value, number {i + 1}: '))
                    y_values.append(ele)
                    break
                except ValueError:
                    print('Please only input numbers')

        return y_values

    x = generate_x()
    y = generate_y()

    print('\nTHE COORDINATES: ')

    def print_x_y_coordinates(x_vals, y_vals):
        for i, j in zip(x_vals, y_vals):
            print(f'({i}, {j})', end=', ')

    print_x_y_coordinates(x, y)
    plotting_1 = CreateUserLineGraph(x, y)
    plotting_1.create_line_graph()

    linegraph_1 = GenerateLineGraph()
    linegraph_1.create_line_graph()
