from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.speed(0)
        self.goto(position)
        
    def move_up(self):
        if(self.ycor() > -260 and self.ycor() < 260):
            self.goto((self.xcor(), self.ycor() + 20))
        
    def move_down(self):
        if(self.ycor() > -260 and self.ycor() < 260):
            self.goto((self.xcor(), self.ycor() - 20))
        
        
        