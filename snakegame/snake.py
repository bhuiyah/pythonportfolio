import turtle 
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT  = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakes = []
        for i in range(3):
            self.add((i*-20, 0))
        self.head = self.snakes[0]
        
    def move(self):
        for i in range(len(self.snakes)-1, 0, -1):
            self.snakes[i].goto(self.snakes[i-1].xcor(), self.snakes[i-1].ycor())
        self.head.forward(MOVE_DISTANCE)
            
    def in_bounds(self):
        return self.head.xcor() < 290 and self.head.xcor() > -300 and self.head.ycor() < 300 and self.head.ycor() > -300
    
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    def add(self, position):
        snake = turtle.Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)
    
    def extend(self):
        for i in range(2):
            self.add(self.snakes[-1].position())
    
    def collision(self):
        for body in self.snakes[1:]:
            if self.head.distance(body) < 8:
                return True
        return False
    
    def reset(self):
        for snake in self.snakes:
            snake.goto((1000, 1000))
        del self.snakes[3:]
        for i in range(3):
            self.snakes[i].goto((i*-20, 0))
    
            
                
            
            
        