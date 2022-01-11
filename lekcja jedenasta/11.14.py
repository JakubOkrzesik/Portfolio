import math


class Calculations():

    @staticmethod
    def circle_surface(radius):
        surface = math.pi*pow(radius,2)
    
        return round(surface,2)

    @staticmethod
    def rectangle_surface(side1,side2):
        surface = side1*side2
    
        return surface

    @staticmethod
    def triangle_surface(base, height):
        surface = (base*height)/2

        return surface

print(Calculations.circle_surface(3))
print(Calculations.rectangle_surface(4,7))
print(Calculations.triangle_surface(6,2))