import json

try:
    with open(r"json Func/Student/Student.json", "r") as f:
        data = json.loads(f.read())
except FileNotFoundError:
    print("File Not Found")
else:
    print(data)