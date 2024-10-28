data = {
    "Name" : "Aftab",
    "Age" : 25,
    "Marks" : [23,56, 78],
    "Sub" : {"a":1, "b":2, "c":3}
}
print(data, "Len is ", len(data))
print(data.items())

data.update({"Add" : 23})
print(data)

dt = data.copy()
print(dt)

ar = [5,4,3,2,1]
ar.sort()
print(ar)