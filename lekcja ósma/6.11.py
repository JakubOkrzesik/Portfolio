array = ["James Bond", "Superbad", "Father Matthew", "Dune"]

file = open('movies.txt', 'w')

file.write('\n'.join(array))

file = open('movies.txt', 'r')

movies1 = file.read()

file.close()

print(movies1)