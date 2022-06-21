from turtle import *
import random
import turtle

tim = Turtle()
tim.shape("circle")
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)   
    return (r,g,b)

def draw_spiro(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.speed("fastest")
        tim.seth(tim.heading() + size_of_gap)

draw_spiro(10)