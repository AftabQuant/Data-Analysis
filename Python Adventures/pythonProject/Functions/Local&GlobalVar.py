# Local Variable

x = 20
print("Before Func : ", x)
def change():
    x = 30
    print("Inside Func : ", x)

change()
print("After Func : ", x)

print()
# Global Variable

x= 20
print("Before Func : ", x)
def change():
    global x
    x = 30
    print("Inside Func : ", x)

change()
print("After Func : ", x)