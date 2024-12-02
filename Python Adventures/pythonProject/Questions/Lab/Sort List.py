arr = [4,3,2,1,5]

asc = sorted(arr)
desc = sorted(arr, reverse=True)
print(asc)
print(desc)

even = list(filter(lambda x: x%2 == 0, arr))
print(even)
