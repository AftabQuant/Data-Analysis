n = int(input("Enter The Number Of Row: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        if i%2 == 0: print(j, end=" ")
        else: print(i, end=" ")
    print()
print()

for i in range(1, n+1):
    for j in range(n+1, i, -1):
        print(i, end=" ")
    print()
print()

# Reverse Triangle
for i in range(1, n+1):
    for j in range(n, i, -1):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

#Reverse Number But Triangle
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
print()
# Two Triangle Together
for i in range(1, n+1):
    for j in range(1, i+1):
        print("&", end=" ")
    print()
for i in range(1, n+1):
    for j in range(n, i, -1):
        print("&", end=" ")
    print()
print()

# Odd Or Even Row Table
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i*j, end=" ")
    print()