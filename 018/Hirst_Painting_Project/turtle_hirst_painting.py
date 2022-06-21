import colorgram
from turtle import *
import turtle
import random


# create a painting 10 x 10 dots
# each dot 20 in size, spaced apart by 50
# find out how to draw circles # fill with random colors
# find out how to move turtle (left to right, start at left again)

# find out the colors in painting
# colors = colorgram.extract('/Users/MichelleA/repos/100-Days/018/Hirst_Painting_Project/hirst_painting.jpg', 30)
# color_list = [(color.rgb.r, color.rgb.g, color.rgb.g) for color in colors]

tim = Turtle()
color_list = [(246, 242, 242), (247, 240, 240), (239, 242, 242), (237, 245, 245), (212, 149, 149), (215, 80, 80), (47, 94, 94), (231, 218, 218), (148, 66, 66), (22, 27, 27), (155, 73, 73), (122, 167, 167), (40, 22, 22), (39, 19, 19), (209, 70, 70), (192, 140, 140), (39, 131, 131), (125, 179, 179), (75, 164, 164), (229, 169, 169), (15, 31, 31), (51, 55, 55), (233, 220, 220), (159, 177, 177), (99, 44, 44), (35, 164, 164), (234, 171, 171), (105, 44, 44), (164, 209, 209), (151, 206, 206)]  
colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()

def draw_painting():
    for _ in range(10):
        dot_color = tim.color(random_color())
        
        dot = turtle.dot(20, dot_color)
        tim.home(-250.00)
        tim.fd(50)

def start_position():
    turtle.penup()
    #turtle.color("white")
    turtle.speed("fastest")
    turtle.goto(-250, -250)



screen = Screen()
screen.exitonclick()
