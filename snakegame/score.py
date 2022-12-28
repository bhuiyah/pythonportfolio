from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 25, "normal")


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto((0, 260))
        self.writescore()
    
    def writescore(self):
        self.write(f"Score: {self.score}", align = ALIGN, font = FONT)
        
    def gameover(self):
        self.goto((0, 0))
        self.write(f"GAME OVER", align = ALIGN, font = FONT)
        
    def add(self):
        self.score +=1
        self.clear()
        self.writescore()