import sys


with open('file.txt', 'r') as f:
    while True:
                
        
        
        x = 0
        
        for line in f:
            
            if line == "\n":
                print("The text has ended")
                sys.exit()
            
            elif x==5:
                break
            print(line, end="")
            x+=1
        y = input("Please press enter if you want to continue, other button to abandon")

        if y!="":
            break 