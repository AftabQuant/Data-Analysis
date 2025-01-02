import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9])
print(array)

# 1D array to 2D array
array_2d = array.reshape(3,3)
print(array_2d)

# Array with zeros
zero = np.zeros(4)
print(zero)

zero_2d = np.zeros((2,2))
print(zero_2d)

# Array with ones
one = np.ones(4)
print(one)

# Empty Array
empty_ar = np.empty(1)
print(empty_ar)

a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
