names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest_name = str(0)

for x in range (len(names) - 1):
    if len(names[x])>len(longest_name):
        longest_name = names[x]
    
separated = ", ".join(names)

print(separated)

print(f"Longest name: {longest_name}")