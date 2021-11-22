import csv

with open('students.txt', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    next(csv_reader)
    
    for line in csv_reader:
        if int(line[2])<30:
            del line[2:4]
            x = " ".join(str(elements)for elements in line)
            print(x)
