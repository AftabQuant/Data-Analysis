s = 0
for i in range(1, 51):
    if i%2 == 0: s += i
print("Sum Of EVen Numbers : ", s)

for i in range(1, 21):
    print(i * i, end=" ")
print()

n = 10
sum = 0
while n>0:
    if n%2 != 0 : sum+=n
    n -=1
print(sum)

for i in range(1, 101):
    if i %8 == 0 and i%12 == 0: print(i)
print()

