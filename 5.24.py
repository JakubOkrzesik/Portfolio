n = float(input("Please enter a number you want to compare: "))

array = [5,6,32,99,125,-5,0]

nums = ''

for x in range(len(array)):
    if n<array[x]:
        nums+= str(array[x]) + ' '
    
print(nums)