def minmax(array):

    minmax1 = []
    minmax1.append(min(array))
    minmax1.append(max(array))

    return minmax1

array = [4,2,8,4,7,9,5]

print(minmax(array))