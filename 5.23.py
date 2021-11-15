import math
import sort as bubblesort


def median(array):
    
    n = len(array)

    if n%2==0:
        return (array[n/2]+array[n/2 - 1])/2
    
    if n%2!=0:
        return array[math.ceil((n-1)/2)]

array1 = [1,0,9,4,6]
array2 = [6,8,3,1,0,5,7]

print(median(array1))
print(median(array2))