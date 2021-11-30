import csv
import json



def txtfile():
    with open("text.txt","r") as f:
        
        x = f.readlines()

        for line in x:
            print(line, end = '')



def csvfile():
    with open("info.csv") as f:
        data = csv.DictReader(f)
        with open("cze.csv", "w", newline='') as g:
            
            fieldname1 = ['first_name','age', 'email']
            
            data1 = csv.DictWriter(g, fieldnames=fieldname1, delimiter = '\t', extrasaction='ignore')

            data1.writeheader()

            for x in data:
                data1.writerow(x)

csvfile()


