from operator import truediv
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

rp = Paddle((350,0))
lp = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkeypress(rp.up,"Up")
screen.onkeypress(rp.down,"Down")
screen.onkeypress(lp.up,"w")
screen.onkeypress(lp.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with walls
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()
        







screen.exitonclick()