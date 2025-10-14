from itertools import count

num = "0123456789"
print(num[:: -1])
print(num[6 :: -1])
print(num.isnumeric())

# Reverse String
s = input("Enter The String : ")
print(s[:: -1])

# To Remove A Given Character From String
a = "HelloWorld!"
b = a.replace("e","")
print(b)

# is Palindrome
s = input("Enter The String : ")
rev = s[:: -1]
if s == rev: print("Palindrome!")
else: print("Not Palindrome !")

# Count The Number Of Vowels
a = "Hello World!"
count = 0
for i in a:
    if i=='a' or i == 'e' or i == 'o':
        count+=1
print(count)
print(a.istitle())