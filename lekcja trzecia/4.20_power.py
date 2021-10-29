def power(x, n):
    num = x * power(x, n-1)
    return num

print(power(5,3))