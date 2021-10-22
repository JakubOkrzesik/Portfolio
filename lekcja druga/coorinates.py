x = int(input("Please enter the x coordinate: "))
y= int(input("Please enter the y coordinate: "))

if x>0 and y>0:
    print(f"The coordinates [{x}, {y}] are in the first quarter")
elif x<0 and y>0:
    print(f"The coordinates [{x}, {y}] are in the second quarter")
elif x<0 and y<0:
    print(f"The coordinates [{x}, {y}] are in the third quarter")
elif x>0 and y<0:
    print(f"The coordinates [{x}, {y}] are in the fourth quarter")
else:
    print(f"The coordinates [{x}, {y}] are in the start point")