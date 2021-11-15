array = [8,2,5,1,9]

separated = ", ".join(array)

print(separated)

print("2ⁿᵈ power: ", end = ' ')
for x in array:
    print(pow(x,2), end =' ')
print()