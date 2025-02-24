def test(*args):
    return args

print(test(1))
print(test(1,2))
print(test(1,2,3,4))
print(test(1,2,3,4,5,6))

def test2(*args, email_id = "aftab.uddin@gmail.com"):
    return args, email_id

print(test2(1,2,3,4))

def test2(*args, email_id):
    return args, email_id

print(test2(1,2,3,4, email_id = "aftab.uddin@gmail.com"))

def test3(**args):
    return args

print(test3(name = "Aftab", email_id="aftab.uddin@gmail.com", phone_no = 12345))