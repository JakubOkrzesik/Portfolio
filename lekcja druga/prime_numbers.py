num = int(input("Please enter a number: "))

x=0

y = 2

prime_nums = 'Prime numbers: '

while x<num-1:
    
    z=2
    
    if y==2:
        prime_nums += str(y) + ' '
    else:
        while z<y:
            if y%z==0:
                break
            z += 1
        else:
            prime_nums += str(y) + ' '
            x+=1
    y+=1
    
    
print(prime_nums)