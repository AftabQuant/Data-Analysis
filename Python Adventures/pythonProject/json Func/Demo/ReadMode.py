import json

with open("Demo.json", "r") as file:
    data = json.load(file)
print(data)