array1 = [4,36,12,28,9,44,5]

array2 = [5,1,36]

z = ''

for x in array1:
    for y in array2:
        if x==y:
            z += str(x) + ' '
            break

print(z)