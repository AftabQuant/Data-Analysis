mini = int(input("Enter The Max Range :  "))
a = 0
b = 1
for i in range(1, mini+1):
    print(a, end=" ")
    c = a + b
    a = b
    b = c