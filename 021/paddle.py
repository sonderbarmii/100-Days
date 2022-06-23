from turtle import Turtle

class Paddle:
.
    def __init__(self):
        self.segments = []


    def create_paddle(self):
        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)