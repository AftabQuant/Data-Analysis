import  re
password = input("Enter Your PassWord : ")
flags = True
if len(password)<8:
    print("Please make strong password !")
    flags = False
elif 8< len(password)< 13:
    if not re.search(r"[a-z]", password): flags = False
    if not re.search(r"[A-Z]", password): flags = False
    if not re.search(r"[0-9]",password) : flags = False
    if not re.search(r"[$#@]", password): flags = False

if flags:
    print("String password")
else: print("Weak password")
