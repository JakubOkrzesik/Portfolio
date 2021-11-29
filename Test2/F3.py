import re

def f3(t):
    x = re.findall(r"\b[1-9][0-9]{1,2}\b", t)

    y = map(int, x)

    z = list(y)

    return sum(z)

t = "Przykładowe liczby parzyste to 16, 2, 114 oraz 1014, a także 8"

print(f3(t))