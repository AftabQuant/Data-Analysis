import re
from re import search

arr = [1, 2, 3, 4, 5, 6, 7]
for i in arr:
    if i == 3:
        print("Found")
        break

print(search(3) in arr)

