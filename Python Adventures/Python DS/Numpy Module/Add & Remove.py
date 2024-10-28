import numpy as np

# Axis 0 refers to the first dimension (rows).
# Axis 1 refers to the second dimension (columns).

ar = np.array([1, 2, 3, 4])
print(np.append(ar, 10))


# insert at index of the array
br = np.array([[1,2,3], [4,5,6]])
print(np.append(br, 50))
print(np.append(br, [65, 70]))
print(np.insert(br, 0, 60)) # array, index, value
print(np.insert(br, 2, [55, 66, 77], axis=0))


# Delete The Array
print(br)
print(np.delete(br, 0, axis = 1))

ls = [1,2,3,4,5,6,7]
print(np.var(ls))
print(np.std(ls))