num = int(input("Enter The Number : "))

for i in range(2, num//2) :
    if num%2 == 0 :
        print("Not")
        break
    else : print("Yes")