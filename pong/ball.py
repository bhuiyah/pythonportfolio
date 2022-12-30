from turtle import Turtle
import random

def top_right():
    return random.randint(30, 50)

def top_left():
    return random.randint(130, 150)

def bottom_right():
    return random.randint(310, 330)

def bottom_left():
    return random.randint(210, 230)

RIGHT = 0
LEFT = 180

directions = [RIGHT, LEFT]#, top_right(), top_left(), bottom_right(), bottom_left()]

class Ball(Turtle):
    
    def __init__(self):
        super().__init__("circle")
        self.goto((0,0))
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.speed(3)
        self.dx = 10
        self.dy = 10
        self.speedup = 0.05
        self.move()
    
    def move(self):
        self.goto((self.xcor() + self.dx, self.ycor() + self.dy))
        
    def paddle_collision(self):
        self.dx *= -1
        self.speedup *= 0.9
        self.move()
        
    def vert_wall_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.dy *= -1
            self.move()
            

    
        
    