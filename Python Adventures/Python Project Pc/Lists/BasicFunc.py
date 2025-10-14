ar = [1, 2, 3, 4, 5, "Apple", "Banana", "Cherry"]

# Length Of List
print("Length Of List Is: ", len(ar))

# Insert Ele In Last
ar.append("Dot")
print(ar)

[print(i, end=" ") for i in ar]
print()

# Insert Ele At Specific Position
ar.insert(5,6)
print(ar)

# Remove Element
ar.remove("Dot")
print(ar)

# Remove Ele Based On Index
ar.pop(5)
print(ar)

# Reverse List
ar.reverse()
print(ar)

# Copy List
a = [1,2,3]
b = a.copy()
print(b)
b.clear()
a.clear()

# Sort List
arr = [3,4,2,5,1]
arr.sort()
print(arr)

# Find Index
print(arr.index(4))
