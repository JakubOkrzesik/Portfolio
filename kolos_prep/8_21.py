import json

with open("euro.json", "r") as f:
    data = json.load(f)

currency = []



for line in data:
    x = line["effectiveDate"]
    z = round(float(line["mid"]) - 0.08,3)
    y = round(float(line["mid"]) + 0.08,3)
    currency.append(x)
    currency.append(y)
    currency.append(z)

print("Date"," "*12,"Buying rate"," "*5,"Selling rate")
print("="*44)
for s in range(0,28,3):
    print(currency[s]," "*6,currency[s+1]," "*10,currency[s+2])