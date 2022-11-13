import matplotlib.pyplot as plt
from random_walk import RandomWalk

if __name__ == '__main__':
    while True:
        random_walk = RandomWalk(50_000)
        random_walk.fill_walk()

        plt.style.use('classic')
        fig, ax = plt.subplots(figsize=(15, 9))
        plt.title('Random Walk Generator')

        # Color the walks with a gradient to determine the direction
        point_nums = range(random_walk.steps)
        ax.scatter(random_walk.x_val, random_walk.y_val, c=point_nums,
                   cmap=plt.cm.Greens, edgecolors='none', s=1)

        # Emphasize first and last points
        ax.scatter(0, 0, c='green', edgecolors='none', s=100)

        ax.scatter(random_walk.x_val[-1], random_walk.y_val[-1],
                   c='red', edgecolors='none', s=100)

        # Turn off axes
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.show()

        # Keep making random walks by user prompt
        keep_running = input("Make another walk? y/n: ")
        if keep_running == 'n':
            break
        elif keep_running == 'y':
            continue
        else:
            print('Input is invalid')
            break



