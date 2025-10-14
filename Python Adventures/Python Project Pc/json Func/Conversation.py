import json

my_data = {'Name': 'Md Aftab', 'Dept': 'Cse-Ds', 'Roll No': '22/cse-ds/032', 'Age': 21, 'CGPA': 8.5}
print(type(my_data))

# Convert dictionary to JSON string
data = json.dumps(my_data)
# json is String Format
print(data)
print(type(data))

# json To Dictionary Format
f = json.loads(data)
print(type(f))
print(f["Name"])

# Read From Existing json File
with open("Details/Details.json", "r") as file:
    read_data = json.load(file)
print(read_data)
