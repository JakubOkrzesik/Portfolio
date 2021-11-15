array = [5,1,9,6,1]

x = max(array)

num = 0

for y in array:
    if y==x:
        continue
    else:
        for z in array:
            if y>z:
                num = y

print(num)
