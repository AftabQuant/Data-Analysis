def divide(a, b) :
    try:
        res = a/b
        print("Result:", res)
    except  ZeroDivisionError :
        print("Error: Cannot divide by zero..")

divide(10,2)
divide(10,0)