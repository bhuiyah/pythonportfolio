from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 40, "bold")


class Score(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.writescore()
    
    def writescore(self):
        self.write(f"{self.score}", align = ALIGN, font = FONT)
        
        
    def add(self):
        self.score +=1
        self.clear()
        self.writescore()
        
    def gameplay(self):
        return self.score < 10
    
        