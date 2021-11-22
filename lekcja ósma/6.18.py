with open('shopping.txt', 'r') as f:
    with open('copy.txt', 'w') as g:
        g.write(f.read())