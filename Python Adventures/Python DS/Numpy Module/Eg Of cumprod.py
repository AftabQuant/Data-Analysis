import numpy as np

price = [100, 150, 199, 200, 250, 130]
quantity = [10, 50, 30, 40, 30, 10]

a = np.array(price)
b = np.array(quantity)
print(a,"\n",b)
print()
c = np.cumprod([price, quantity], axis = 0)
print(c)
print(c[1].sum())
