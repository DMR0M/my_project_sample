import matplotlib.pyplot as plt


class RandomLineGraph:
    def __init__(self):
        self.x_values = range(1, 1001)
        self.y_values = [n**2 for n in self.x_values]

    def create_line_graph(self):
        plt.style.use('fivethirtyeight')
        flg, ax = plt.subplots()
        plt.title('User Created Line Graph: ')
        # ax.plot(self.x_values, self.y_values)
        ax.scatter(self.x_values, self.y_values, c=self.y_values, cmap=plt.cm.Blues, s=10)
        ax.axis([0, 1100, 0, 1100000])
        print(self.x_values)
        plt.show()


if __name__ == '__main__':
    graph_1 = RandomLineGraph()
    graph_1.create_line_graph()
