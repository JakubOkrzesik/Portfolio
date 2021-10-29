def sum_digits(n):  
    sum = 0
    while (n != 0):
       
        sum = sum + (n % 10)
        n = n//10
       
    return sum

n = 7182
print(sum_digits(n))
