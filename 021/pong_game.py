from operator import truediv
from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

p1 = Paddle()

screen.listen()
screen.onkeypress(p1.up,"Up")
screen.onkeypress(p1.down,"Down")

game_is_on = True
while game_is_on:
    screen.update()







screen.exitonclick()