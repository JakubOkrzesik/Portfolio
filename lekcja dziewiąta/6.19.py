expressions = []

while True:
    print("Enter '=' to end the expression")
    x = input("Please enter a number or operator: ")
    if x=="=":
        expressions.append(x)
        break
    elif type(x)==int:
        expressions.append(int(x))
    else:
        expressions.append(x)

stack = []

def isnum(x):
    try: 
        int(x)
        return True
    except:
        return False



for y in expressions:
    if isnum(y):
        stack.append(y)
    elif y=="=":
        print(f"The result is: {stack.pop()}")
    else:
        f = int(stack.pop())
        s = int(stack.pop())
        if y=="+":
            r = f + s
            stack.append(r)
        elif y=="-":
            r = f-s
            stack.append(r)
        elif y=="*":
            r = f*s
            stack.append(r)
        elif y=="/":
            r = f/s
            stack.append(r)
    