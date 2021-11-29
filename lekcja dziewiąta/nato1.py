from xdd import nato

x = input("Please enter your phrase: ")

for y in x.upper():
    for z in nato.keys():
        if z==y:
            print(nato[z], end=' ')

