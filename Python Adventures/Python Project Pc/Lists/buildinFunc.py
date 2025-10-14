import ast

arr = [1, 2, 3, 4, 5, "Apple", "Banana"]
print(arr)

print("Length Of List: ", len(arr))
print(arr.count(2))

# insertion Element
arr.append("Cherry")
print(arr)

# Add At Specific Location
arr.insert(5,6)
print(arr)

# Remove Element
arr.remove(6)
print(arr)

# Remove At Specific Element
print(arr.pop(1)) # index
print(arr)
arr.insert(1,2)
print(arr)
print()
# Copy Of The Lists
brr = arr.copy()
print(brr)
arr[0] = 100
print(brr)
print(arr)

# To Find index
print(arr.index(4))

# To Extend The List
arr.extend(brr)
print(arr)

# Reverse List
arr.reverse()
print(arr)

# Sort The List
a = [3,4,1,2,5]
a.sort()
print(a)

# To Clear All Data
a.clear()
print(a)