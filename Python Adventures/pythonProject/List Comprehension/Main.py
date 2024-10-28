a = [30, 40, 50, 60]

# Copy List To Another New List
b = [i for i in a if i > 45]
print(b)

# Square using list comprehension
square = [x**3 for x in range(1,10)]
print(square)

grt = list([x for x in square if 20<x<90])
print(grt)

