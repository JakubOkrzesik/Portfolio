import turtle
import random


siema = turtle.Turtle()

siema.shape('turtle')

siema.color('blue', 'red')

def circlesandshit():
    for x in range(7):
        siema.begin_fill()
        siema.circle(100)
        siema.penup()
        siema.goto(random.randint(-300,300), random.randint(-300,300))
        siema.pendown()
        siema.end_fill()
        
    turtle.done()

circlesandshit()