import turtle
import time
import score
from paddle import Paddle
import ball

screen = turtle.Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

right_score = score.Score((50, 230))
left_score = score.Score((-50, 230))

right_paddle = Paddle((380, 0))
left_paddle = Paddle((-390, 0))

myBall = ball.Ball()

def check_key():
    screen.onkey(right_paddle.move_up, "Up")
    screen.onkey(right_paddle.move_down, "Down")
    screen.onkey(left_paddle.move_up, "w")
    screen.onkey(left_paddle.move_down, "s")

def horizontal_collision():
    if(myBall.xcor() > 400):
        left_score.add()
    elif(myBall.xcor() < -400):
        right_score.add()   
    myBall.goto((0, 0))
    myBall.speedup = 0.05
    
    
while left_score.gameplay() and right_score.gameplay():
    time.sleep(myBall.speedup)
    screen.update() 
    check_key()
    myBall.move()
    if (myBall.distance(right_paddle) < 35 and myBall.xcor() < 390) or (myBall.distance(left_paddle) < 35 and myBall.xcor() > -390):
        myBall.paddle_collision()
    myBall.vert_wall_collision()
    if myBall.xcor() > 400 or myBall.xcor() < -400:
        horizontal_collision()
        right_paddle.goto((380, 0))
        left_paddle.goto((-390, 0))
        
if not left_score.gameplay():
    left_score.goto((0, 0))
    left_score.write(f"Left Player Wins.", align = score.ALIGN, font = score.FONT)
    
if not right_score.gameplay():
    right_score.goto((0, 0))
    right_score.write(f"Right Player Wins.", align = score.ALIGN, font = score.FONT)  
    
screen.exitonclick()             
