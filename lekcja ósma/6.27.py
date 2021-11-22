import re

with open("shoppinglist.txt", "r") as f:
    for line in f:
        x = re.findall("[A-Za-z]{6,}", line)
        if x==[]:
            continue
        else:
            print(x)