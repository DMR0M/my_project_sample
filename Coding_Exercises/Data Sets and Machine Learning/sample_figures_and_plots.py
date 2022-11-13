import matplotlib.pyplot as plt

squares = [1, -4, 9, -16, 25, -36, 49, -64, 81, -100]
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
# flg, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=100)
flg1, ax1 = plt.subplots()
ax1.plot(squares)
# ax.set_title('Square Numbers', fontsize=24)
# ax.set_xlabel('Value', fontsize=14)
# ax.set_ylabel('Square of Value', fontsize=14)
# ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

