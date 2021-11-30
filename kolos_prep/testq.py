import json

with open("students.json", "r") as f:
    data = json.load(f)
    

with open("limited.json", "w") as f:
    for line in data:
            print(line["name"])