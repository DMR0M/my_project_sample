import numpy as np

# a = [1, 2, 3]
# b = [3, 4, 6]

# int (int16) = 2 bytes/per item
# int (int32) = 4 bytes/per item
# float (int64) = 8 bytes/per item

a = np.array([1, 2, 3, 5, 17])
b = np.array([3.0, 4.0, 6.0, 8.0, 10.0])
c = np.array([[6.2, 9.5, 3.4, 10], [5.6, 7.4, 10.5, 5.0]])
d = np.array([[4, 1, 2], [9, 5, 8]], dtype='int16')  # Setting int types
# print(a * b)

# Getting Shape
rows_cols = c.shape

# Getting Dimensions
dims = c.ndim

# Getting Type
a_type = a.dtype
b_type = b.dtype

# Getting Item sizes
a_item_size = a.itemsize
b_item_size = b.itemsize
c_item_size = c.itemsize

# Getting No. items
a_size = a.size
b_size = b.size

# Getting Total size of all items
a_total = a.size * a_item_size
b_total = b.size * b_item_size

# Or bytes
a_byte_total = a.nbytes
b_byte_total = b.nbytes
d_byte_total = d.nbytes

print(f'Size of a:\n{a_byte_total}\n'
      f'Size of b:\n{b_byte_total}\n'
      f'Size of d:\n{d_byte_total}\n'
      f'Total size of array a:\n{a_total}\n'
      f'Total size of array b:\n{b_total}\n'
      f'Items of a:\n{a_size}\n'
      f'Items of b:\n{b_size}\n')
# print(f'Data type of a:\n{a_type}\n'
#       f'Data type of b:\n{b_type}\n'
#       f'Item size of a:\n{a_item_size}\n'
#       f'Item size of b:\n{b_item_size}\n'
#       f'Item size of c:\n{c_item_size}\n')
print(f'Number of dimensions:\n{dims}')
print(f'Number of rows and columns:\n{rows_cols}')

