x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x>y:
    print(f"Numbers in ascending order: {y}, {x}")
elif y>x:
    print(f"Numbers in ascending order: {x}, {y}")
else:
    print(f"Numbers {x} and {y} are equal")