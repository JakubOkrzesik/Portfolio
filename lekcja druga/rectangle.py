a = int(input("Please enter side a of the rectangle: "))
b = int(input("Please enter side b of the rectangle: "))

if a<0 or b<0:
    print("Please enter a natural number")
    a = int(input("Please enter side a of the rectangle: "))
    b = int(input("Please enter side b of the rectangle: "))
    
x=0
while x<a:
    x = x+1
    if x==1 or x==a:
        print('*'*b)
    else:
        print('*' + ' '*(b-2) + '*')
        