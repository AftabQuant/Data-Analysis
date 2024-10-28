import numpy as np

# 1D Array
arr = np.array([10, 20, 30, 40])
# brr = np.array(([1,2,3,4]))
print(arr)

# Slicing
print(arr[0:3])
print(arr[::-1])

#2D Array
arr = np.array([[1,2,3,7],[4,5,6,8]])
print(arr)
print(arr[0, 0:2])
print(arr[0:2, ::-1])
print(arr[::-1, 0:2])

# Attributes Of Array
arr = np.array([[1,2,3,7],[4,5,6,8],[10,11,12,13]])
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))
print(arr.dtype)

# Operations In Array
arr = np.array([10, 20, 30, 40])
brr = np.array(([1,2,3,4]))
print(arr+brr)
print(arr - brr)
print(arr * brr)
print(arr // brr)

# Concatenate Two Array
arr = np.array([[10, 20], [30, 40]])
brr = np.array(([[1,2],[3,4]]))
print(np.concatenate([arr, brr], axis=0))
print(np.vstack([arr,brr]))
print()
print(np.concatenate([arr, brr], axis=1))
print(np.hstack([arr, brr]))

# Split
arr = np.array([[10, 20, 3], [30, 40, 5]])
b = np.array_split(arr,2)
print(b)

# Insert & Delete Element
arr = np.array([1,2,3,4,5,6,7,8])
print(np.append(arr, 9))
print(np.insert(arr, 5,  [100, 150]))
print(np.delete(arr, [6,2]))

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(np.insert(arr, 0, 10, axis=1))
print(np.delete(arr,0, axis= 0))

# Sort , Search
arr = np.array([11,2,31,4,54,6])
print(np.sort(arr))
print(np.where(arr == 4))

# Filter The Array
arr = np.array([11,2,31,4,54,6])
print(list(filter(lambda x: x%2==0, arr)))

price = np.array([100, 150, 140, 200, 250])
quantity = np.array([2,5,8,15,3])

c = np.cumprod([price, quantity], axis=0)
print("Total Sum Is : ", np.sum(c[1]))
print(np.std(price))
















