file = open('numbers.txt', 'r')

nums = 0

for line in file:
    nums+=int(line)

file.close()

print(nums)