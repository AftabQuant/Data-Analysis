import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr)
print()
brr = np.reshape(arr,(2,3))
print(brr)

print(np.sum(brr, axis=0))

r = (1,2,3,3)
ar = np.array(r)
print(r)