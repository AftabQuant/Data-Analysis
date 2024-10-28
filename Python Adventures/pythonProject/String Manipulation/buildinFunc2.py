a = "Hello World"
b = "Hello 123   *"
c = "123456"
d = "HELLO"
e = " "
f = "1.234"
g = 1.234

# endswith() : if string ends with specified values
print(a.endswith("llo"))
print(a.endswith("el"))

# startswith() : if string starts with specified values
print(a.startswith("Hel"))

# strip() : Trimmed Version Of String
print(b.strip("*"))

# ljust() : Return a left version of the String
x = a.ljust(20)
print(x, " Is first program")

# rjust() : Return a right version of the String
x = a.rjust(20)
print( x, " Is first program")

# replace() : replace word
print(a.replace("Hello", "Helloo"))

# rindex() : Last Index Of where it was found
print(a.rindex("o"))

# slicing
print(a[0: 6])
print(a[6: len(a)])
print(a[6: ])
num = "0123456789"
print(num[:: 2])

# Reverse Of String
print(num[:: -1])
print(num[6 :: -1])