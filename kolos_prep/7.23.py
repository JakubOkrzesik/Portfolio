import csv

with open('info.csv', 'r') as f:
    data = csv.DictReader(f)

    with open('limited.csv', 'w', newline='') as g:
        fieldnames1 = ['first_name','last_name', 'email']
        data1 = csv.DictWriter(g,fieldnames=fieldnames1, delimiter = '\t', extrasaction='ignore')        

        data1.writeheader()

        for x in data:
           data1.writerow(x)
                