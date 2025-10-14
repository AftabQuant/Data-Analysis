# Find max element From # elements
def maximum(a, b, c):
    if a > b and a > c : print(a)
    elif b> a and b > c: print(b)
    else: print(c)

# Store 1 to 30's square in the list
arr = []
for i in range(1, 31):
    arr.append(i ** 2)

for i in arr:
    print(arr, end=" ")

def fun():
    print("Hello World!")
def add(a, b):
    return a+b
print(add(7.9,8))
fun()
print(add(5,8))
