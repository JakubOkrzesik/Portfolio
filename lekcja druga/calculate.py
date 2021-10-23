q=0
sum = 0
mean = 0
x=1

while x>0:
    
    x = int(input("Enter number: "))
    if x==0:
        break
    q += 1
    sum += x
    mean = sum/q
    
    
print(f"RESULT: Quantity={q}, Sum={sum}, Mean={mean}")