def coins(price):
    
    coins_amount = 0
    
    coins_amount += price//5
    x = (price//5)*5
    price = price%x
    
    coins_amount += price//2
    x = (price//2)*2
    price = price%x
    
    coins_amount += price//1
    
    
    return coins_amount


print(coins(22))