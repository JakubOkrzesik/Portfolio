import math

class Point(): 
    def __init__(self,x,y): 
        self.x = x 
        self.y = y 
    
    
    def __str__(self): 
        return f'P({self.x},{self.y})'
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return 'Distance between points is 0'
        else:
            distance = math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))
            return 'The distance between points is: ' + str(distance)
            

first = Point(210,210)

second = Point(-210, 210)

print(first == second)



