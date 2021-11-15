array = [15,8,31,47,2,19]

x = len(array)

converted_array = [str(element) for element in array]


separated = ", ".join(converted_array)

print(f"existed array: {separated}")


print("reverse array: ", end = ' ')

while x>0:
    print(array[x - 1], end = ' ')
    x-=1
print()    

