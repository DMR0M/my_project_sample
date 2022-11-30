import numpy as np


def matrix(a: np.array):
    return a


if __name__ == '__main__':
    arr_a = np.array([[5, 6, 4, 8, 10, 12], [50, 10, 20, 5, 7], [67, 18, 2]], dtype='object')
    # print(matrix(arr_a))

    # Accessing Matrices
    mat_x = np.array([[1, 5, 6], [9, 7, 3], [4, 0, 8]])
    mat_a = np.array([[1, 2, 3, 4, 10], [5, 6, 7, 8, 19], [9, 10, 11, 12, 22]])
    print(mat_a)
    fave_num: int = mat_x[2, 2]  # Row num + Col num
    f_row: int = mat_x[0, :]
    f_column: int = mat_x[:, 2]
    a_row: int = mat_a[1, 1:4]  # 1st row, column from index 1 to 3
    print(a_row)
    # print(fave_num)
    # print(f_row, f_column)


