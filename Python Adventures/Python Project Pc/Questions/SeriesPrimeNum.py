low = int(input("Enter min range : "))
high = int(input("Enter max range : "))
for i in range(low, high+1):
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:
                break
        else :
            print(i)
# n = int(input("Enter Num :  "))
# if n == 1:
#     print("np")
# elif n == 2 : print("p")
# else:
#     for i in range(2, n+1):
#         if n % i == 0:
#             print("p")
#             break
#         else:
#             print("np")
#             break

        for j in range(2, 8):
            if 9 % j == 0:
                break