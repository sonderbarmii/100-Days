import turtle

class Snake:

    def __init__(self,  name):
        self.name = name

    # create a snake body
    def create_snake(self):
        for position in starting_positions:
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        segments.append(snake)
    
starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []
    # snake moves # tail follows head
    def move_forward(self):
        for seg_num in range(len(segments) -1, 0, -1): #start (we want to start at 2), stop, step
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x,new_y)
        segments[0].forward(20)