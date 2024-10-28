# Concatenate Two Array
import numpy as np
ar = np.array([[10, 20], [30,40]])
br = np.array([[1, 2],[3, 4]])
cr = np.concatenate([br, ar])
print(cr)

# hstack : Horizontal Concatenation
print(np.hstack([br, ar]))

# vstack : Vertical Concatenation
print(np.vstack([br, ar]))

# split : Split The Array
cr = np.array([1,2,3,4,5,6,7,8,8])
xr = np.array_split(cr,3)
print(xr)
print(xr[1])