from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto((-270, 260))
        self.writescore()

    def writescore(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)
    
    def add(self):
        self.score +=1
        self.writescore()
        
    def reset(self):
        self.score = 0
        self.writescore()