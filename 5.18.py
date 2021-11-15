def bubblesort(array):
    
    n = len(array) - 1
    
    for x in range(n):

        for y in range(n - x):

            if array[y]>array[y+1]:
                array[y], array[y+1] = array[y+1], array[y]
        
    return array