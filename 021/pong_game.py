from turtle import Screen


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

p1 = Paddle()

screen.listen()
screen.onkey(paddle.up,"Up")
screen.onkey(paddle.down,"Down")









screen.exitonclick()