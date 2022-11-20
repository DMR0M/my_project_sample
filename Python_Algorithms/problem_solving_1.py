import matplotlib.pyplot as plt


def calculate_trajectory(x):
    loc = 10*x - 5*(x ** 2)
    return loc


xs = [x/100 for x in list(range(201))]
ys = [calculate_trajectory(x) for x in xs]
plt.plot(xs, ys)
plt.title('the trajectory of a thrown ball'.title())
plt.xlabel('horizontal position of a ball'.title())
plt.ylabel('vertical position of a ball'.title())
plt.axhline(y=0)
plt.show()
