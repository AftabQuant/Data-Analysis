n = int(input("Enter The Number Of The Table: "))
print("Using For Loop")
for i in range(1, 11):
    print(n * i, end=" ")
print()
# Is Odd Or Even Number
for i in range(1, 10):
    if i%2 == 0:
        print(i, end=" ")
print()

# Table Using while loop
print("Using While Loop")
a = 1
while a<=10:
    print(a * n, end=" ")
    a +=1