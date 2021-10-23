num = int(input("Please enter a number: "))

x=1

while x<num-1:
    
    x += 1
    
    factor = num%x
    
    if factor==0:
        print(f"{num} is not a prime number")
        
    elif x == num - 1:
        print(f"{num} is a prime number")
    