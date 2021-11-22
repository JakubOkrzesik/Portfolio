array = ["Jakub", "Okrzesik", "UEK Cracow", "Applied Infromatics"]

file = open('info.txt', 'w')

file.write('\n'.join(array))

file = open('info.txt', 'r')

file1 = file.read()

file.close()

print(file1)