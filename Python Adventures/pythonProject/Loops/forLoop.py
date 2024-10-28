n = int(input("Enter The Range: "))
for i in range(1, n):
    print(i)
    print("Hello World !")

# 2 Steps increment
for i in range(1, n, 2) :
    print(i, "Hello World !")

# continue Statement
for i in range(1, n):
    if i%2 == 0: continue
    else: print(i)