from turtle import Turtle

STARTING_POSITION = (350,0)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:

    def __init__(self):
        self.create_paddle()
        # x_pos = 350
        # y_pos = 0
        self.penup()
        self.goto(STARTING_POSITION)

    def create_paddle(self):
        self.paddle = self.shapesize(stretch_wid=20, stretch_len=100, outline=None)

        # for position in starting_positions:
        #     new_segment = Turtle("square")
        #     new_segment.color("white")
        #     new_segment.penup()
        #     new_segment.goto(position)
        #     self.segments.append(new_segment)

    def up(self):
        if self.paddle.heading() != DOWN:
            self.paddle.setheading(UP)

    def down(self):
        if self.paddle.heading() != UP:
            self.paddle.setheading(DOWN)