def f1(a):
    
    y=0
    
    for x in a:
        if x%2==0 and x>8:
            y+=1
        else:
            continue
    return y


a = [13,7,4,16,3,12,8]

print(f1(a))