human_age = int(input("Please enter the dog's age in human years: "))

if human_age<0:
    print("Please enter a natural number")
    human_age = int(input("Please enter a number that is positive: "))

dog_age = 0

x = 1

if human_age<=2:
    while  x <= human_age:
        dog_age = dog_age + 10.5
        x += 1
else:
    dog_age = human_age*4 - 8 + 21
    
print(f"The dog's age in dog’s years is {dog_age} years.")
    