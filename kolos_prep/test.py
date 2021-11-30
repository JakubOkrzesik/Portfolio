import json

with open("students.json", "r") as f:
    data = json.load(f)
    

with open("limited.json", "w") as f:
    
    x = 0
    for x in range(500):
        del data[x]["gender"]
        del data[x]["age"]
        del data[x]["year of study"]
        del data[x]["email"]
    json.dump(data, f)