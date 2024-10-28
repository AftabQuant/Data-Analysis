s = input("Enter A String : ")
for i in range (0, len(s)):
    for j in range(0, i+1):
        print(s[j], end=" ")
    print()

# Odd & Even Position Character

for i in range(len(s)):
    if i % 2 == 0:
        print( s[i], end=" ")
print()
for i in range(len(s)):
    if i % 2 != 0:
        print( s[i], end=" ")
print()

# Merge Two String
a = "abc {}"
b = "cde"
c = "fgh"
print(a.format(b))

