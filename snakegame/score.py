from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 25, "normal")


class Score(Turtle):
    
        
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto((-200, 260))
        self.writescore()
    
    def writescore(self):
        self.goto((0, 260))
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align = ALIGN, font = FONT)
        
    def gameover(self):
        self.updatehighscore()
        self.writescore()
        self.goto((0, 0))
        self.write(f"GAME OVER", align = ALIGN, font = FONT)
        self.goto((0, -30))
        self.write(f"Try again? Press 'c'", align = ALIGN, font = FONT)
        self.updatehighscore()
        
    def add(self):
        self.score +=1
        self.clear()
        self.writescore()
        
    def updatehighscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.highscore))