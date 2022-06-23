from turtle import Turtle

STARTING_POSITION = (350,0)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:

    def __init__(self):
        paddle = self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(paddle.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(paddle.xcor(), new_y)