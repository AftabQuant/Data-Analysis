my_data = {}
for i in range(1, 16):
    my_data[i] = i**2
print(my_data)

# Multiply All Items In Dictionary
mul = 1
for i in my_data.keys():
    mul *= i
print(mul)