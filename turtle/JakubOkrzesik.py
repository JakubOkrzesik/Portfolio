import turtle
import random


class Shapes():
    
    color = ''
    xcords = 0
    ycords = 0
    

    @staticmethod
    def stopabstractart():
        turtle.done()

# Outputs the name and album number of the creator of this program
    
    @staticmethod
    def saynmyname():
        
        bob = turtle.Turtle()
        bob.speed(0)
        bob.hideturtle()
        bob.penup()
        bob.goto(80,300)
        bob.pendown()
        bob.color('black')
        bob.write('Jakub Okrzesik, 221507', font=('Courier', 20, 'normal'))



# Assigns a random hexadecimal number to self.color that results in a random color being genrated
    @staticmethod
    def setrandomcolor():
        hexa = '1234567890ABCDEF'

        Shapes.color = '#'
        

        for x in range(6):
            Shapes.color += random.choice(hexa)

# Every time this function is called the coordinates will be randomized
    @staticmethod
    def setrandomcords():
        Shapes.xcords = random.randint(-200,200)
        Shapes.ycords = random.randint(-200,200)
    
    
# Draw a square by specifying the length of the sides
    @staticmethod
    def drawsquare(length, *color):
        
        bob = turtle.Turtle()

        bob.hideturtle()


        if Shapes.color!='':
            bob.color(Shapes.color)
            bob.begin_fill()

        elif color!=():
            bob.color(Shapes.color)
            bob.begin_fill()


        bob.penup()
        bob.goto(Shapes.xcords, Shapes.ycords)
        bob.pendown()

        
        

        for x in range(4):
            bob.forward(length)
            bob.left(90)
        
        bob.end_fill()  

        


#draw a regular polygon by calling the function and entering the length of the sides and the number of them
    @staticmethod
    def drawregularpolygon(length, sidenumber, *color):
        
        bob = turtle.Turtle()


        bob.hideturtle()


        if Shapes.color!='':
            bob.color(Shapes.color)
            bob.begin_fill()

        elif color!=():
            bob.color(color)
            bob.begin_fill()


        bob.penup()
        bob.goto(Shapes.xcords,Shapes.ycords)
        bob.pendown()
        
        

        for x in range(sidenumber):
            bob.forward(length)
            bob.left(360/sidenumber)
        
        bob.end_fill()
        

    
#draw a heart enterng the radius of the circles that make the heart
    @staticmethod
    def drawheart(length, *color):
        
        bob = turtle.Turtle()

        bob.hideturtle()


        if Shapes.color!='':
            bob.color(Shapes.color)
            bob.begin_fill()

        elif color!=():
            bob.color(color)
            bob.begin_fill()

        bob.penup()
        bob.goto(Shapes.xcords,Shapes.ycords)
        bob.pendown()
        

        bob.shape('turtle')
        bob.left(90)
        bob.circle(length,225)
        bob.forward(2.4*length)
        bob.left(90)
        bob.forward(2.4*length)
        bob.circle(length,225)
        bob.end_fill()
        bob.hideturtle()


#Function draws a randomized polygon with random coordinates and a random color
    
    @staticmethod
    def drawrandomizedpolygon():
        #generating random coordinates, number of sides and angle as well as length for each side
        xcords = random.randint(-200,200)
        ycords = random.randint(-200,200)
        sides = random.randint(3,8)
        angle = random.randint(0,360)
        
        Shapes.setrandomcolor()

        bob = turtle.Turtle()


        bob.hideturtle()

        bob.penup()
        bob.goto(xcords,ycords)
        bob.pendown()
        
        bob.color(Shapes.color)

        bob.begin_fill()
        for x in range(sides-1):
            bob.left(angle)
            bob.forward(random.randint(10,100))
        
        bob.goto(xcords,ycords)
        
        bob.end_fill()


#function draws randomized triangle 
    @staticmethod
    def drawrandomtriangle(*color):
        
        bob = turtle.Turtle()

        bob.hideturtle()

        if Shapes.color!='':
            bob.color(Shapes.color)
            bob.begin_fill()

        elif color!=():
            bob.color(color)
            bob.begin_fill()

        
        bob.penup()
        bob.goto(Shapes.xcords,Shapes.ycords)
        bob.pendown()
        
        angle = random.randint(1,179)
        bob.left(angle)
        bob.forward(random.randint(10,100))
        bob.left(random.randint(1,180 - angle))
        bob.forward(random.randint(10,100))
        bob.goto(Shapes.xcords,Shapes.ycords)
        
        bob.end_fill()
        
#The funcitons generates a canvas including some of the previously mentioned shapes randomly. To stop the animation press the space bar
        
    @staticmethod
    def abstractart():
        shape_decider = random.randint(1,4)
        
        Shapes.setrandomcolor()
        Shapes.setrandomcords()

        if shape_decider==1:
            Shapes.drawsquare(random.randint(20,100))
        elif shape_decider==2:
            Shapes.drawrandomizedpolygon()
        elif shape_decider==3:
            Shapes.drawrandomtriangle()
        elif shape_decider==4:
            Shapes.drawregularpolygon(random.randint(20,50), random.randint(5,10))
        


        Shapes.abstractart()

    @staticmethod
    def onkeyspace():
        turtle.listen()

        bob = turtle.Turtle()

        bob.hideturtle()
        
        bob.penup()

        bob.speed(0)

        bob.goto(-350, 300)

        bob.pendown()

        bob.write('To stop the animation press space', font=('Courier', 20, 'normal'))

        turtle.onkey(Shapes.stopabstractart, 'space')

x = Shapes()


x.onkeyspace()
x.saynmyname()
x.abstractart()

# turtle.done() needs to be called at all times for the program to function
turtle.done()


