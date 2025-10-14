import json

with open("Details.json", "r") as f:
    data = json.loads(f.read())
print(data)