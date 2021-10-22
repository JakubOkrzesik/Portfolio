cash = int(input("Please enter the amount of money you want to calculate: "))

if cash<0:
    print("Please enter a natural number")
    cash = int(input("Please enter the amount of money you want to calculate: "))
sum = 0
amount_5 = 0
while sum<cash:
    sum = sum + 5
    amount_5 = amount_5 + 1
    if sum>cash:
        amount_5 = amount_5 - 1
        sum = sum - 5
        break
amount_2 = 0

while sum<cash:
    sum = sum + 2
    amount_2 = amount_2 + 1
    if sum>cash:
        amount_2 = amount_2 - 1
        sum = sum - 2
        break
amount_1 = 0

while sum<cash:
    sum = sum + 1
    amount_1 = amount_1 + 1
    if sum>cash:
        amount_1 = amount_1 - 1
        sum = sum - 2
        break
print(f"{amount_5}, {amount_2}, {amount_1}")