array = [2, 3, 2, 5, 8, 1, 9, 8]

nums = ''

n = len(array) - 1

for x in range(n):
    z = 0
    y = 0
    while y<=n:
        if x==y:
            y+=1
            continue
        
        else:
            if array[x]==array[y]:
                z+=1
            y+=1
                
    if z==0:
        nums += str(array[x]) + ' '

og_array = " ".join([str(v) for v in array])

print(f"Array: {og_array}")
print(f"Unique elements: {nums}")