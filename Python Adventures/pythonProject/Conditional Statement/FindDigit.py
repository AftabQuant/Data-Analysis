num = int(input("Enter The Number: "))
if 0 <= num <= 9:
    print(num," is a single digit number !")
elif 10 <= num <= 99:
    print(num, "is a 2 digit number !")
elif 100 <= num <= 999:
        print(num, " is a 3 digit number !")
elif 1000 <= num <= 9999:
        print(num, "is a 4 digit number !")
else :
    print(num," is a 5 digit number")