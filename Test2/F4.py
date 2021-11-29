def f4(d):
    num_sum = 0
    for x in d:
       for y in d[x]:
           if y>=5 and y<=10:
               num_sum+=y

    return num_sum

print(f4({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}))