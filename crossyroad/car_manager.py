from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.increment = MOVE_INCREMENT
        self.add_car()
         
    def add_car(self):
        #time.sleep(1)
        if len(self.cars) < 35:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_len = 2)
            car.speed(0)
            car.goto((random.randint(300, 1000), random.randint(-250, 250)))
            car.color(random.choice(COLORS))
            self.cars.append(car)
        
    def move_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.goto((random.randint(300, 1000), random.randint(-250, 250)))
            car.goto(car.xcor() - self.increment, car.ycor())
            
    def level_up(self):
        self.increment = STARTING_MOVE_DISTANCE + MOVE_INCREMENT
        
        