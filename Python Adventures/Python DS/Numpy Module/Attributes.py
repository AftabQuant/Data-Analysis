# Shape Of Array
import numpy as np

ar = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print("Shape of the array: ", ar.shape) # rows, columns
print("Size Of Array: ",ar.size)

# Give Dimensions Of The Array
print("Dimensions : ",np.ndim(ar))

print("Length Of The Array: ",len(ar))

print(ar.astype(float)) # Conversion Of Data Type