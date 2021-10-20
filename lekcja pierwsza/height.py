
x = input("Please enter your height: ")
height = int(x)

h_feet = height*0.0328
y = int(h_feet)
h_inches = h_feet % 1
z = int(round(h_inches, 1)*10)

print(f"I am {height} tall, i.e. {y} feet and {z} inches.")