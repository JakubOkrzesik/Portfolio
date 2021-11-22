with open('nums.txt', 'w') as f:
    for x in range(1,51):
        
        if x==50:
            f.write(str(x))
        else:
            y = str(x) + "\n"
            f.write(y)
        