import json

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

data = json.dumps(my_data, indent=4, separators=(",", ": "))
with open("Student.json", "w") as f:
    f.write(data)

with open("Student.json", "r") as f:
    data = json.loads(f.read())
print(data)