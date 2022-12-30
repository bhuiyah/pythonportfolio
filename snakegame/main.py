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
score = Score()

def reset():
    screen.tracer(0)
    score.score = 0
    score.clear()
    score.writescore()
    snake.reset()
    game()
      
def check_key():
    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_right, "Right")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(reset, "c")
    
def game():
    game_is_on = True 
    while game_is_on:
        screen.update() 
        time.sleep(0.05)
        check_key()
        snake.move()
        if snake.head.distance(food) < 15:
            food.move()
            snake.extend()
            score.add()
        if not snake.in_bounds() or snake.collision():
            game_is_on = False
    score.gameover()          
     
game()

    
         
screen.exitonclick()
