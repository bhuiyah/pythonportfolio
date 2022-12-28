from turtle import Turtle
import random
class Food(Turtle):
    
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.move()
    
    def move(self):
        self.goto((random.randint(-270, 270), random.randint(-270, 240)))

