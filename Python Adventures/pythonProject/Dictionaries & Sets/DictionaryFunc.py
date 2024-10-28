my_data = {"Name": " Aftab", "Age": 32, "Id ": "22/cse-ds/032"}

# get : Give value of key
x = my_data.get("Name")
print(x)

# item : Give key & value
a = my_data.items()
print(a)

# key: Give All key
b = my_data.keys()
print(b)

# key: Give All Value
c = my_data.values()
print(c)

# copy
d = my_data.copy()
print(d)

# pop
my_data.pop("Name")
print(my_data)