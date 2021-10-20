a = input("Enter the length of the first side: ")
b = input("Enter the length of the second side: ")
c = input("Enter the length of the third side: ")

p = int((int(a)+int(b)+int(c))/2)

S = (p*(p-int(a))*(p-int(b))*(p-int(c)))**(1/2)

print(S)