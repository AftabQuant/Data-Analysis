def display(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
    print()
display(5)