x = int(input("Please enter a number: "))

y = 0

stack = []

while x!=0:
    if x%2==0:
        stack.append(0)
    else:
        stack.append(1)
    x = x//2

for z in range(len(stack)):
    print(stack.pop(), end='')
print()