import math

# GCD Of Two Number
def gcd(a, b):
    minimum = min(a, b)
    for i in range(minimum, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

a = int(input("Enter The 1st Number :  "))
b = int(input("Enter The 2nd Number :  "))
print("GCD Of This Two Numbers  is : ", gcd(a, b))

# LCM Of Two Number
x = int(input("Enter The 1st Number :  "))
y = int(input("Enter The 2nd Number :  "))

z = (x *y) / gcd(x, y)
print(z)


