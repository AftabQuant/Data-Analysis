arr = [1, 2, 3, 4, 5, "apple", "banana"]
print(type(arr))
print(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")
print()
print(arr[:: -1])
print(arr[1: 5])
print(arr[-1: -5:-1])

brr = [10, 20, 30.0, "A", "B", "C"]
print(brr)

for i in brr: print(i, end=" ")
print()

brr.append("D")
print(brr)

brr.insert(3, 40.5)
print(brr)

brr.remove("D")
print(brr)

brr.pop(3)
print(brr)

brr.reverse()
print(brr)
brr.reverse()

crr = brr.copy()
print(crr)

print(crr.index(30.0))