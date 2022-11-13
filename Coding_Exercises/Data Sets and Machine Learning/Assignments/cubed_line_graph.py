import matplotlib.pyplot as plt


class CubedLineGraph:
    """Graph that shows the cubed coordinates"""
    def __init__(self):
        self.x_val = range(1, 5001)
        self.y_val = [n**3 for n in self.x_val]
        self.coordinates = list(zip(self.x_val, self.y_val))

    def show_line_graph(self):
        plt.style.use('fivethirtyeight')
        fig, ax = plt.subplots()
        plt.title('Cubed Numbers Line Graph: ')
        # ax.plot(self.x_val, self.y_val, linewidth='3')
        ax.scatter(self.x_val, self.y_val, c=self.y_val, cmap=plt.cm.Greens, s=30)
        plt.show()


if __name__ == '__main__':
    graph_1 = CubedLineGraph()
    print(graph_1.coordinates)
    graph_1.show_line_graph()
