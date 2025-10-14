import json

my_data = {"Name " : ["Aftab", "Imran", "Ariful", "Irfan"],
           "Age" : [20,17,15,19],
           "Course" : ["DS", "AIML","CS","CC"]}
# Write json File
data = json.dumps(my_data, indent=4, separators=(",", ":"))
with open("Data.json", "w") as f:
    f.write(data)

