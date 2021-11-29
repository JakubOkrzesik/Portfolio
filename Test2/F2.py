def f2(a1,a2):
    
    count_a1 = 0
    
    count_a2 = 0

    for x in a1:
        if len(str(x))==2:
            count_a1+=1

    for x in a2:
        if len(str(x))==2:
            count_a2+=1
    
    return count_a2==count_a1


print(f2([23,7,16,34],[1,18,79,2,6,111]))           