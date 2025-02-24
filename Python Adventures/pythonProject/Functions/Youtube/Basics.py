def test():
    print("This is my first function...")
test()

def test1(x,y):
    print(x,y) # print return a NoneType datatype
test1(y="world", x="hello ")

def test2(a,b,c):
    return a,b,c
print(test2("Aftab", "Cse-Ds", 32))
print(type(test2("Aftab", "Cse-Ds", 32)))

m, n, v = test2("Aftab","Cse-Ds",32)
print(m,n,v)
print(type(m), type(n), type(v))

def test3(nums):
    for i in nums:
        print(i, end=" ")
test3([1,2,3,4,5,6])

