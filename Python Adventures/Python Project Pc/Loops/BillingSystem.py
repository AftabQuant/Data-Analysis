while True:
    name = input("Enter Your Name: ")
    total = 0
    while True:
        print("Enter Price And Quantity")
        amount = float(input("Enter The Amount : "))
        quantity = float(input("Enter The Quantity: "))
        amount = amount * quantity
        total += amount
        repeat = input("Do you want to add more items[Yes Or No] : ")
        if repeat == "no" or repeat == "No": break
    print("Name: ", name)
    print("Total Amount: ", total)
    break