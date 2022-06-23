from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed(MOVE_DISTANCE)
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
     
    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_at_goal(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

