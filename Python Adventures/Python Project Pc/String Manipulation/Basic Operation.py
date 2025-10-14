s = "Hello World"
print(s)
print(s[:: -1])
print(s)

for i in range(len(s)):
    print(s[i], end=" ")
print()

a = "Hello {}"
b = " World !"
print(a.format(b))
for i in range(len(s)):
    for j in range(0, i+1):
        print(s[j], end=" ")
    print()