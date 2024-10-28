import numpy as np

ar = np.array([20, 40, 50, 60, 70, 80])


# sum of the values
print(np.sum(ar))


# min and max values
print(np.min(ar))
print(np.max(ar))

# size or count of values
print(np.size(ar))

# mean of the values
print(np.mean(ar))

# cumulative sum of the values
print(np.cumsum(ar))

br = np.array([[10,20,30],[40, 50, 60]])
print(np.sum(br))
print(np.mean(br))
print(np.cumsum(br))