def hello():
    print("Hello World !")

hello()

def add(x, y): # x, y are called Parameter
    return x+y

print(add(2,3)) # 2,3 are called Argument
print(add(4.5,7.9))

def list_print(arr):
    print(arr)

# Arbitrary Argument
def hello(* name):
    print(name)

hello("A","b","V")

# key value types of argument
# def fun(dc):
#     print(dc)
# dic = {
#     "name":"Aftab",
#     "Age" : 20,
#     "Marks":89.9
# }
# fun(dic)

def fun(ch3, ch1, ch2):
    print(ch1, ch2, ch3)
fun(ch1 = "A", ch2="B", ch3 = "C")
print()

# arbitrary key-value pairs
def fun(**ch):
    print(ch)
fun(ch1 = "A", ch2="B", ch3 = "C")

# Lambda Function
add = lambda a,b : a+b
res = add(34,5)
print(res)