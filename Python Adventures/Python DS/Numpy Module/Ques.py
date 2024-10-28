import numpy as np
arr = [1,2,3,4,5,6,7, 8, 9]
print(arr)

brr = np.array(arr)
print(brr)

x = int(input("Enter the value : "))
brr = np.delete(brr,x) # x is index 
print(brr)

arr = np.array([[3,2,1],[6,5,4],[9,8,7]])

print(np.sum(arr, axis = 1))

y = int(input("Enter the value : "))
print(y in arr)

# 1D Array To 2D Array
brr = np.array([1,2,3,4,5,6,7, 8, 9])
print(brr)
crr = brr.reshape(3,3)

print(crr)

c = (1,2,3,4,5,6)
print(c, type(c))
cr = np.array(c)
print(cr)