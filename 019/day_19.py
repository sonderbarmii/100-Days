from turtle import *

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.fd(10)

screen.listen()
screen.onkey(fun=move_forwards,key="space")