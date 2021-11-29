def f5(c):
    
    sum_c = 0
    
    with open("poem.txt", "r") as f:
        x = f.read()
        for line in x:
            for y in line:
                if y.lower() == c:
                    sum_c+=1 
            
    return sum_c

print(f5("m"))