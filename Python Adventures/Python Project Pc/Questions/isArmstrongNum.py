def arms(n):
    x = n
    res = 0
    order = len(str(n))
    while n > 0:
        rem = n % 10
        res += rem ** order
        n //= 10
    if res == x : print("A")
    else: print("NA")

num = int(input("Enter The Number :  "))
arms(num)

def largest(ar):
    ar.sort()
    print(ar[-1])


ar = [4,2,5,1,3]
largest(ar)
