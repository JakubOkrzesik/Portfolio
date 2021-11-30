import csv

def f6(g,n1,n2):
    with open("people.csv", "r") as f:
        
        counter = 0

        x = csv.DictReader(f)
        for row in x:
            if row['gender']==g and int(row['age'])>=n1 and int(row['age'])<=n2:
                counter+=1

    return counter
print(f6("Female",160,180))