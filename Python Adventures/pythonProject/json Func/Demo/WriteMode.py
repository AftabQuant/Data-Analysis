import json

data = {'Name': "Md Aftab", "Age": 20, "Marks": 85, 'Course': 'Cse-Ds'}
file = open("Demo.json", "w")
s = json.dumps(data, indent=3, separators=(",", ": "))
file.write(s)

f = open("Demo.json", "w+")
sb = json.dumps(data, indent=3, sort_keys= True)
f.write(sb)
