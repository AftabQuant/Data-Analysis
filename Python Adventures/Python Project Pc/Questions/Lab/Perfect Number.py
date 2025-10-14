num = int(input("Enter The Number : "))
sum = 0
for i in range(1, num):
    if i%2 == 0 : sum +=i
if sum == num : print("P")
else: print("NP")