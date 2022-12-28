import turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()

      
def check_key():
    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_right, "Right")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_down, "Down")

score = Score()

while snake.in_bounds() and not snake.collision():
    screen.update() 
    time.sleep(0.05)
    check_key()
    snake.move()
    if snake.head.distance(food) < 15:
        food.move()
        snake.extend()
        score.add()
            
score.gameover()  
    
         
screen.exitonclick()
