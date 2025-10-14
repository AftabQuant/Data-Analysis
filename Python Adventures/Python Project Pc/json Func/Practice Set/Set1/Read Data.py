import json

# Read json File
with open("Data.json", "r") as f:
    data = f.read()

dt = json.loads(data)
print(dt, type(dt))