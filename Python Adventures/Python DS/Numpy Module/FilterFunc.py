import numpy as np

ar = np.array([20, 30, 40, 50])
fa = [True, False, True, False]
res = ar[fa]
print(res)

fa = ar > 35
res = ar[fa]
print(res)

fa = ar%2 == 0
res = ar[fa]
print(res)