n = [12,6,4,9,3]

def star(n):
    
    z = ""
    
    for x in n:
        y = '*'* x
        z += str(x) + ':' + str(y) + '\n'

    return z
print(star(n))


