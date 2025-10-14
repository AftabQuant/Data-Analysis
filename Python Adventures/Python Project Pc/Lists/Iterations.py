arr = [1, 2, 3, 4, 5, "apple", "banana"]
print(arr)

# for Loop
for i in arr:
    print(i, end=" ")
print("\n")

for i in range(len(arr)):
    print(arr[i], end=" ")
print("\n")

i = 0
while i < len(arr):
    print(arr[i], end=" ")
    i +=1
print("\n")

# Short Hand for Loop
[print(i, end=" ") for i in arr]
