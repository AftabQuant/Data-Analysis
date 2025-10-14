arr = []

n = int(input("Enter The Size : "))
for i in range(0, n) :
    ele = int(input())
    arr.append(ele)
print(arr[0:])
for i in range(0, n):
    print(i - len(arr),end = " ")

print()
print(arr[0])
print(arr[-1])