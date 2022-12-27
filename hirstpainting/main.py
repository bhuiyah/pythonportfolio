import colorgram
import turtle
import random

# colors = colorgram.extract('hirst.jpg', 30)

# colorList = []
# for i in range(len(colors)):
#     colorList.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))


colors = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)] 

# 10x10 painting, each circle is 20 in size and 50 spaces apart

myTurtle = turtle.Turtle()
myScreen = turtle.Screen()
myScreen.colormode(255)
myTurtle.speed(0)

myTurtle.penup()
myTurtle.hideturtle()
myTurtle.setheading(225)
myTurtle.forward(300)
myTurtle.setheading(0)

x = myTurtle.xcor()
for i in range(10):
    y = myTurtle.ycor()
    for j in range(10):
        randcolor = random.choice(colors)
        myTurtle.dot(20, randcolor)
        # myTurtle.pencolor(randcolor)
        # myTurtle.fillcolor(randcolor)
        # myTurtle.begin_fill()
        # myTurtle.pendown()
        # myTurtle.circle(20)
        # myTurtle.penup()
        # myTurtle.end_fill()
        myTurtle.forward(50)
    
    myTurtle.sety(myTurtle.ycor() + 50)
    myTurtle.setx(x)
    
        
        

myScreen.exitonclick()
        

