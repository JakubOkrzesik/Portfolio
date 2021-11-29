from xdd import nato

with open("ICAO.txt", "w") as f:
    for x,y in nato.items():
        z = x + ' ' + y + "\n"
        f.write(z)

with open("ICAO.txt", "r") as f:
    print(f)