from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    # create a snake body
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.segments.append(new_snake)
    
    # snake moves # tail follows head
    def move_forward(self):
        for seg_num in range(len(self.segments) -1, 0, -1): #start (we want to start at 2), stop, step
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)