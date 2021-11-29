import csv

def f6(g,n1,n2):
    with open("people.csv", "r") as f:
        
        counter = 0

        x = csv.reader(f)
        for row in x:
            if row[3]==g and int(row[2])>=n1 and int(row[2])<=n2:
                counter+=1

    return counter
print(f6("Female",160,180))