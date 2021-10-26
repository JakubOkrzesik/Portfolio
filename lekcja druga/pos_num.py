x = int(input("Please enter first number: "))
y = int(input("Please enter your second number: "))

if x>=0 and y>=0:
    print("Both numbers are positive")
elif x>=0 and y<0:
    print("First number is positive and second negative")
elif x<0 and y>=0:
    print("First number is negative and second is positive")
