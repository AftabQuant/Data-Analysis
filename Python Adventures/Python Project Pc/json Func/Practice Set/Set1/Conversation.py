import json

my_data = {"Name " : ["Aftab", "Imran", "Ariful", "Irfan"],
           "Age" : [20,17,15,19],
           "Course" : ["DS", "AIML","CS","CC"]}
print(my_data)

# Dic To Json Format
data = json.dumps(my_data)
print(data)

# Json Format To Dic
data = json.loads(data)
print(data)