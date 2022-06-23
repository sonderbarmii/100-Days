from operator import truediv
from turtle import Screen
import time
from player import Player

screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.title("Turtle Crossing Game")

tim = Player()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()




screen.exitonclick()