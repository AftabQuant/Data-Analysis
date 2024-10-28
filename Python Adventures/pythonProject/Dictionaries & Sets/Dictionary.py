my_data = {"Name": " Aftab", "Age": 32, "Id ": "22/cse-ds/032"}
print(my_data)

# Print All Key
for i in my_data:
    print(i, end=" ")
print()

# Print All Values
for i in my_data:
    print(my_data[i], end=" ")
print()
for i in my_data.values():
    print(i, end=" ")

# Print Key-Values Both
for i, j in my_data.items():
    print(i, j)


