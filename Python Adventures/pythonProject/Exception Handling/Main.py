try:
    n = float(input("Enter 1st Number :  "))
    m = float(input("Enter 2nd Number :  "))
    res = n/m
except ZeroDivisionError:
    print("Can't Divide By Zero")
else:
    print("Result is :  ", res)