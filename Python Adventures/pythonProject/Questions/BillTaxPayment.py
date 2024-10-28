amount = int(input("Enter The Amount : "))
Total_amount = 0
if amount <= 800:
    print("You Will Pay : ", amount)
elif 800<= amount <=1200:
    tax = amount * (10/ 100)
    Total_amount = amount + tax
    print("You will pay : ", Total_amount)
elif 1200<= amount <=2000:
    tax = amount * (15 / 100)
    Total_amount = amount + tax
    print("You will pay : ", Total_amount)
else:
    tax = amount * (22 / 100)
    Total_amount = amount + tax
    print("You will pay : ", Total_amount)
