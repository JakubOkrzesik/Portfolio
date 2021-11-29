import json

with open("data.json") as f:
    data = json.load(f)

for k,v in data.items():
    print(k,':',v)
print()