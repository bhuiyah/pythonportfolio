import turtle
import random

colors = ["tomato", "peru", "dark green", "dark magenta", "red", "aquamarine", "blue", "green", "coral", "dark slate blue", "dark turquoise", "dark olive green", "gold"]

turtle.colormode(255)
    
directions = [0, 90, 180, 270]
    
def draw_square(turtle):
    for i in range(0, 4):
        turtle.forward(100)
        turtle.right(90)

def draw_dashed(turtle):
    for i in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

def draw_shapes(turtle):
    for i in range(3, 11):
        turtle.color(random.choice(colors))
        for j in range(0, i):
            turtle.forward(100)
            turtle.right(360/i)
            
def random_walk(turtle):
    turtle.pensize(10)
    turtle.speed(10)
    for i in range(200): 
        turtle.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.forward(15)
        turtle.setheading(random.choice(directions))
             

timmy = turtle.Turtle()

#draw_square(timmy)
#draw_dashed(timmy)
#draw_shapes(timmy)
random_walk(timmy)


myScreen = turtle.Screen()
myScreen.exitonclick()