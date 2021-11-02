import random

def rand(fr0m, to):
    
    y=1
    
    while y>0:
        x = random.randint(fr0m, to)
        if x%2==0 and x%3==0:
            break
        else:
            y+=1
    
    return x


print(rand(10,50))