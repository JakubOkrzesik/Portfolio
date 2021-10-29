def numcheck():
    n = int(input("Please enter a number: "))
    x = int(input("Enter the first number of the range: "))
    y = int(input("Enter the second number of the range: "))
    return n >= x and n<=y

print(numcheck())