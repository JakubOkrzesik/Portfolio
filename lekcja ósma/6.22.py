with open('nomanshouldhaveallthatpower.txt', 'w') as f:
    for x in range(1,11):
        z = str(x)+ ", " + str(pow(x,2)) + ", " + str(pow(x,3)) + '\n'
        f.write(z)