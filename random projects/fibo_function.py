## Triple Fibonacci

def t_fibo(n):
    y = 0
    z = 1
    for x in range(n):
        if x<=1:
            print(x, end=' ')
        else:
            q = y + z
            print(q, end=' ')
            y = z
            z = q
    print()
    
t_fibo(10)