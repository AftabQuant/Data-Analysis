import numpy as np

a = np.random.randint(1,10,4)
b = np.random.randint(1,10,4)
a_2d = a.reshape(2,2)
b_2d = b.reshape(2,2)
print(a_2d,"\n")
print(b_2d,"\n")
# Axis 0 => column
c_2d = np.concatenate([a_2d,b_2d], axis=0)
print(c_2d,"\n")

# Axis 1 => rows
c_2d = np.concatenate([a_2d,b_2d], axis=1)
print(c_2d)


