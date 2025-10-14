# a = ["Ross", "Rachel", "Monica", "Joe"]
#
# a[0], a[3] = a[3], a[0]
# print(a)
#
# a.insert(1, "New")
# print(a)
#
# b = [13, 7, 12, 10]
# b.pop(2)
# print(b)
#
# mul = 1
# for i in b:
#     mul *= i
# print(mul)
#
# b.sort()
# print(b)
# print("Largest Value: ",b[-1])
# print("Smallest Value: ",b[0])

num = list(range(1, 11))
print(num)
print("Even Num Are : ")
for i in num:
    if i%2 == 0:
        print(i, end=" ")

