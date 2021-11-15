array = [4,6,3,32,5,7,112]

array1 = [4,112,32,5]

array2 = [32,7,112,113,45]

z = 0

for x in range(len(array1)):
    for y in range(len(array)):
        if array1[x] == array[y]:
            z+=1

if z==len(array1):
    print("The second array is a subset of the first one")

else:
    print("The second array is not a subset of the first one")

