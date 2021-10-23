n = int(input("Please enter the amount of interations: "))

x = 0
y = 1

fibo = '0' + ' ' + '1' + ' ' 

for i in range(1,n):
    c = x + y
    x=y
    y=c
    fibo += str(y) + ' ' 
    
print(fibo)