set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8,9,10}
set3 = {3,5,2,4,1}

# Sort The Set
set3 = sorted(set3)
print(set3)

# Min & Max Element
print("Min Element is : ", set3[0])
print("Max Element is : ", set3[-1])

# Common Element
print(set1.intersection(set2, set3))

# Difference Element
print(set1.difference(set2))

# Remove Element If Present In Set
ele = 2
for i in set3:
    if i == ele : set3.remove(i)
print(set3)

# is subset or not
set1 = {1,2,3,4,5,6}
set2 = {2,3,4}
print(set2.issubset(set1))