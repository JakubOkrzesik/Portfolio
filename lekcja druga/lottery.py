import random

numbers = ' '

for x in range(1, 8):
    
    for y in range(1,8):
            
        z = random.randint(1, 49)
        
        numbers += str(z) + ' '
    
    coupon = str(x) + numbers
    
    numbers = ' '
    
    print(coupon)