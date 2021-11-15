array = [2,5,6,7,90,31,14,15,16]

array1 = []

for x in array:
    if x%2==0:
        array1.append(x)
        array.remove(x)

final_array = array1 + array

print(final_array)