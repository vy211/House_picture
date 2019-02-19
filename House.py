#    @Vipin Yadav


import turtle
import math
screen=turtle.Screen()
screen.bgcolor("Skyblue")

george=turtle.Turtle()
george.color("black")
george.shape("turtle")
george.speed(10)

#define a function for draw rectangle
def drawRectangle(t,width,height,color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    
#define a function for draw triangle
def drawTriangle(t,length,color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()


#define a function for draw parallelogram
def drawParallelogram(t,width,length,color):
    t.fillcolor(color)
    t.begin_fill()
    t.left(30)
    t.forward(width)
    t.left(60)
    t.forward(length)
    t.left(120)
    t.forward(width)
    t.left(60)
    t.forward(length)
    t.left(90)
    t.end_fill()


# front wall of house
george.penup()
george.goto(-150,-120)
george.pendown()
drawRectangle(george,100,110,"blue")

# door
george.penup()
george.goto(-120,-120)
george.pendown()
drawRectangle(george,40,60,"lightgreen")

# front triangle wall
george.penup()
george.goto(-150,-10)
george.pendown()
drawTriangle(george,100,"magenta")

# side wall
george.penup()
george.goto(-50,-120)
george.pendown()
drawParallelogram(george,60,110,"#DC143C")

# window
george.penup()
george.goto(-30,-80)
george.pendown()
drawParallelogram(george,20,50,"red")

# side roof
george.penup()
george.goto(-50,-10)
george.pendown()
george.fillcolor("orange")
george.begin_fill()
george.left(30)
george.forward(60)
george.left(105)
george.forward(100/math.sqrt(2))
george.left(75)
george.forward(60)
george.left(105)
george.forward(100/ math.sqrt(2))
george.left(45)
george.end_fill()

# sun
george.penup()
george.goto(-180,180)
george.fillcolor("Yellow")
george.begin_fill()
george.pendown()
george.circle(50)
george.end_fill()




# For draw the Tree

george.penup()
george.goto(115,-75)
drawRectangle(george,60,150,"#401C1C")
george.penup()
george.color("green")
george.goto(90,40)
george.fillcolor("Green")
george.begin_fill()
george.pendown()
george.circle(60)
george.penup()
george.goto(210,40)
george.pendown()
george.circle(80)
george.goto(110,100)
george.circle(60)
george.end_fill()


# turtle in front of door             
george.penup()
george.goto(-100,-150)
george.left(90)








