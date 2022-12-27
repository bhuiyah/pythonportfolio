from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for i in range(0, 6):
   turt = Turtle(shape="turtle")
   turt.color(colors[i])
   turt.penup()
   turt.goto(-230, -100 + i*30)
   turtles.append(turt)

race_on = False
user_bet = screen.textinput("Make your bet!", "Which one are you betting on to win? ").lower()

if user_bet:
    race_on = True

while race_on:
    for i in range(6):
        if turtles[i].xcor() > 230:
            race_on = False
            if(turtles[i].pencolor() == user_bet):
                print(f"You were right! The {turtles[i].pencolor()} turtle is the winner!")
            else:
                print(f"You were wrong! The {turtles[i].pencolor()} turtle is the winner.")   
        turtles[i].forward(random.randint(0, 10))
    
      
    
screen.exitonclick()