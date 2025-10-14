# Temporary Function But Only Expression
# func = lambda b : b * 5
# print(func(5)) # 25
#
#
# func2 = lambda a,b : a * b
# print(func2(5,6)) # 30

add = lambda *ele: sum(ele)
res = add(1,2,3,4)
print(res)

res = list(map(lambda x: x*2, [1,2,3,4]))
print(res)