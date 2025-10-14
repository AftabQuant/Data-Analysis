while True:
    print("1 For Area Of Square")
    print("2 For Area Of Rectangle")
    print("3 For Area Of Circle")
    print("4 For Area Of Triangle")
    choice = int(input("Enter Your Choice B/w 1 And 4 : "))
    while True:
        if choice == 1:
            a = float(input("Enter The Side Of Square : "))
            res1 = a * a
            print("Area Of Square: ", res1)
        elif choice == 2:
            length = float(input("Enter The Length Of Rectangle : "))
            wid = float(input("Enter The Width Of Rectangle : "))
            res2 = length * wid
            print("Area Of Rectangle Is : ", res2)
        elif choice == 3:
            r = float(input("Enter The Radius Of Circle : "))
            res3 = (22/ 7) * r * r
            print("Area Of Circle: ", res3)
        elif choice == 4:
            b = float(input("Enter The Base Of Triangle : "))
            h = float(input("Enter The Height Of Triangle : "))
            res4 = (h * b) / 2
            print("Area Of Triangle: ", res4)
        repeat = input("Do You Want Try Once More Time [Yes/ No]: ")
        if repeat == "No" or repeat == "no": break

    repeat = input("Do You Want Find Another Area Once More Time [Yes/ No]: ")
    if repeat == "No" or repeat == "no": break