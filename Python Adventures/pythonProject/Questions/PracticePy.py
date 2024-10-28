# power of a number
# x = int(input("Enter The Base : "))
# y = int(input("Enter The Power : "))
# print("Result is :  ",x ** y)
from itertools import count
from pydoc import apropos

# Even Or Odd
# x = int(input("Enter The Number : "))
# if x%2 == 0:
#     print(x, " is an even number")
# else:
#     print(x, " is an odd number")

#Largest Three
# x = int(input("Enter The Number : "))
# y = int(input("Enter The Number : "))
# z = int(input("Enter The Number : "))
# print(max(x, y, z))

# Fizz Or Buzz
# for i in range(1, 101):
#     if i%3 == 0: print(i, " Fizz")
#     elif i%5 == 0: print(i, " Buzz")
#     elif i%3==0 and i%5==0: print(i, " FizzBuzz")

# Sum of the list
# ar = [1,2,3,4,5,6]
# print(sum(ar))

# Avg Of The list
# ar = [1,2,3,4,5,6]
# print(sum(ar)/ len(ar))

# Max Of The List
# ar = [1,2,3,4,5,6]
# print(max(ar), min(ar))

#Swap Two Numbers
# def swap(a, b):
#     return b,a
# x = 10
# y = 20
# # x,y = y,x
# x,y = swap(x,y)
# print(x, y)

# Count Word & store occurrence in dict
# st = "hello World hello World "
# word = st.split()
# dic = {}
# for i in word:
#     if i in dic:
#         dic[i] +=1
#     else:
#         dic[i] = 1
# print(dic)

# Merge two dict
# dic1 = {
#     "name ": "hello"
# }
# dic2 = {
#     "hel ": "aftab"
# }
# res = {**dic1, ** dic2}
# print(res)

# Anagram Or Not
# s = input("Enter 1st St : ")
# t = input("Enter 2nd St : ")
# if sorted(s) == sorted(t):
#     print("Anagram")
# else:
#     print("Not Anagram")

# st = "Hello World!"
# count = 0
# for i in st:
#     count +=1
# print(count)

# Factorial Num
# def fac(n):
#     if n==1: return 1
#     return n * fac(n-1)
# num = int(input("Enter Number : "))
# print(fac(5))

# Prime Number
# def prime(n):
#     for i in range(2, n+1):
#         if n%i == 0:
#             print("Not Prime")
#             break
#         else:
#             print("Prime Num")
#             break
# prime(7)

# Fibonacci Series
# def fibo2(n):
#     if n<2: return n
#     return fibo2(n-1) + fibo2(n-2)
# def fibo(n):
#     a = 0
#     b = 1
#     c = 0
#     for i in range(0, n+1):
#         print(a, end=" ")
#         c = a+b
#         a = b
#         b = c
# fibo(10)
# print()
# print(fibo2(6))

# GCD and LCM
def gcd(m,n):
    mn = min(m, n)
    for i in range(mn, 0, -1):
        if n % i == 0 and m % i == 0:
            return i
def lcm(m,n):
    return (m*n)/gcd(m,n)

n = int(input("Enter Number : "))
m = int(input("Enter Number : "))
print(gcd(n, m))
print(lcm(n,m))
