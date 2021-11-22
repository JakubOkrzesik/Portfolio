with open('shopping.txt', 'a') as file:
    while True:
        x = input("Please enter an item. Enter 0 to stop: ")
        if x== "0":
            break
        file.write(x + '\n')

with open('shopping.txt', 'r') as file:
    x = file.read()
    print(x, end='')