from turtle import Turtle, Screen

myTurtle = Turtle()
screen = Screen()


def move_forwards():
    myTurtle.forward(5)

def move_back():
    myTurtle.back(5)
    
def turn_right():
    myTurtle.setheading(myTurtle.heading() - 10)
    
def turn_left():
    myTurtle.setheading(myTurtle.heading() + 10)

def clear():
    myTurtle.clear()
    myTurtle.penup()
    myTurtle.home()
    myTurtle.pendown()
    myTurtle.setheading(heading)
    
x = myTurtle.xcor()
y = myTurtle.ycor()
heading = myTurtle.heading()

myTurtle.speed(0)
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
