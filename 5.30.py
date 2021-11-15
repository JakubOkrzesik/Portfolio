import random

def rand_elem(array):
    return array[random.randint(0,len(array) - 1)]




array = [*range(1,999)]

print(rand_elem(array))