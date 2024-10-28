num = int(input("Enter The Number Of Terms : "))
a = 0
b = 1
c = 0
for i in range(1,num+1):
    print(a)
    c = a + b
    a = b
    b = c

# Palindrome or not
n = int(input("Enter The Number Of Terms : "))
temp = n
rev = 0
while temp > 0:
    rev = rev*10 + temp % 10
    temp = temp // 10

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

