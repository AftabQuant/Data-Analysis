def pattern(n):
    nsp = n-1
    nst = 1
    for i in range(1, n+1):
        for j in range(1, nsp+1):
            print("  ", end=" ")
        for j in range(1, i+1):
            print("*", end=" ")
        print()
        nsp -=1
        nst +=2

pattern(5)