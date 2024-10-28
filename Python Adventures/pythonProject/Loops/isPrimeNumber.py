num = int(input("Enter The Number  : "))
if num<= 1:
    print("It is not a prime number!")
else:
    for i in range(2, num):
        if num%i == 0:
            print(" Not Prime Number ! ")
            break
        else:
            print(" Prime Number !")
            break