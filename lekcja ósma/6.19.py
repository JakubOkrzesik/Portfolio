with open('MeatAndFish.txt', 'r') as f:
    with open('shoppinglist.txt', 'a') as h:
        h.write(f.read())

with open('GrainsAndBread.txt', 'r') as g:
    with open('shoppinglist.txt', 'a') as h:
        h.write(g.read())
