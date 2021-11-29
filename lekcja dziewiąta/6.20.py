import json

with open("students.json", "r") as f:
    data = json.load(f)
    

with open("limited.json", "w") as f:
    for line in data:
            del data[3]
            del data[4]
            del data[5]
            del data[6]
    json.dump(data, f)
