# data = open('data.txt', 'r+')
# print(data.read())
#
# data.write('\nModified by using python.')
# print(data.read())

import numpy as np
c = np.array([6, 7, 5, 8])
d = np.array([4, 3, 7, 8])
pro = c.dot(d)
print(pro)