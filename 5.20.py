def occurs(number, array):
    
    n = len(array)
    
    for x in range(n):
        if number==array[x]:
            return number
            break
    
    return "The number doesn't appear in the array"
    

array = [15, 38, 7, 23, 14]
number = 60

print(occurs(number, array))