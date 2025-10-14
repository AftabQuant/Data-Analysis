def prime(num):
    if num == 1 : print("np")
    if num == 2 : print("p")
    if num > 2:
        for i in range(2, num):
            if num%i == 0:
                print("p")
                break
            else:
                print("np")
                break
print(prime(12))

# sum of all elements of the list
def add(ar):
    if len(ar) == 1 : return ar[0]
    return ar[0] + add(ar[1: ])
ar = []
n = int(input("Enter The Size Of The List: "))
for i in range(0, n):
    ele = int(input("Enter The Element Of The List: "))
    ar.append(ele)
print(ar)
print(add(ar))
