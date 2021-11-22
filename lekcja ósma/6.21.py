import random

with open('randomnums.txt', 'w') as f:
    for x in range(50):
        if x==49:
            f.write(str(random.randint(100,999)))
        else:
            y = str(random.randint(100,999)) + '\n'
            f.write(y)