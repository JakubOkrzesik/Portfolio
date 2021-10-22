y = ' '
for x in range(1,31):
    if x%3==0 and x%5==0:
        y += 'BINGO' + ' '
    elif x%5==0:
        y += 'FIVE' + ' '
    elif x%3==0:
        y += 'THREE' + ' '
    else:
        y += str(x) + ' '
        
print(y)