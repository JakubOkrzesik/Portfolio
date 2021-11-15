colors = ["blue", "yellow", "green", "black", "brown"]

f = open("colors.txt", "a")

for x in range (len(colors) - 1):
    f.write(colors[x] + '\n')

f = open("colors.txt", "r")

print(f.read())