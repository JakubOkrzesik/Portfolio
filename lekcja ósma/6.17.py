with open('countries.txt', 'r') as f:
    
    x=''
    
    for line in f:
        x+=line


with open('copyline.txt', 'w') as g:
    g.write(x)