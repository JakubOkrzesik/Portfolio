import re

with open("grades.txt", "r") as f:
    x = f.read()
    y = re.findall("[1-9][.][0-9]", x)
    sum_num = 0
    for element in y:
        sum_num+=float(element)
    
    print(sum_num/len(y))
        