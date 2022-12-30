import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
score = Scoreboard()
manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move_up, "Up")
    manager.add_car()
    manager.move_cars()
    if player.ycor() > 300:
        player.sety(-280)
        score.add()
        manager.level_up()
    for car in manager.cars:
        if player.distance(car) < 18:
            game_is_on = False
            
score.goto((-100, 0))           
score.write(f"Your Score: {score.score}", font=("Courier", 24, "bold"))           

screen.exitonclick()