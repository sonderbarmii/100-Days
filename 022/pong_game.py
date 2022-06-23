from operator import truediv
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

rp = Paddle((350,0))
lp = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(rp.up,"Up")
screen.onkeypress(rp.down,"Down")
screen.onkeypress(lp.up,"w")
screen.onkeypress(lp.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # detect collision with paddles
    if ball.distance(rp) < 50 and ball.xcor() > 320 or ball.distance(lp) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # detect when r paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect when l paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()