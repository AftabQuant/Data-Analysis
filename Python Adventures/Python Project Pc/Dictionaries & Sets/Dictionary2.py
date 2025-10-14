dic = {"Name": "Aftab", "Age": 20, "Course": "Cse-Ds"}
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

print(dic.get("Name"))


for i in dic:
    print(dic[i])

for i in dic.items(): print(i)
print()

my_data = {
    "People 1" :[
        {"Name": "Aftab",
         "Age": 20,
         "Course": "Cse-Ds"
         },
        {"Name": "Aftab",
         "Age": 20,
         "Course": "Cse-Ds"
         },
    ],
    "People 2": [
        {"Name": "Aftab",
         "Age": 20,
         "Course": "Cse-Ds"
         },
        {"Name": "Aftab",
         "Age": 20,
         "Course": "Cse-Ds"
         },
    ]
}
print(my_data)

print(my_data["People 1"][1]["Age"])

for i in my_data:
    print(my_data[i][1]["Course"])