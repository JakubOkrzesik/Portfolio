with open('countries.txt', 'r') as f:
    
    line_counter = 0

    for line in f:
        if line!="\n":
            line_counter+=1
        else:
            break


print("File name: ",f.name)
print(f"Number of lines: {line_counter}")