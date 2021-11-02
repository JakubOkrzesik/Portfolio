def bonus(years):

    money = 0
    
    x = 1
    
    while x<=years:
    
        if x<=5:
            money += 100
            
        elif x>5 and x<=8:
            money += 200
            
        else:
            money += 50
            
        x += 1
    
    return money

print(bonus(9))