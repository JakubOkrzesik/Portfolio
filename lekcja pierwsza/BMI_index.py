height = input("Please enter your height in centimeters: ")
weight = input("Please enter your weight in kilograms: ")

x = float(height)/100
y = int(weight)

BMI = y/(x**2)

print(round(BMI, 2))