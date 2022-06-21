import colorgram
from turtle import *
import turtle
import random

# find out the colors in painting
# colors = colorgram.extract('/Users/MichelleA/repos/100-Days/018/Hirst_Painting_Project/hirst_painting.jpg', 30)
# color_list = [(color.rgb.r, color.rgb.g, color.rgb.g) for color in colors]

tim = Turtle()
color_list = [(239, 242, 242), (237, 245, 245), (212, 149, 149), (215, 80, 80), (47, 94, 94), (231, 218, 218), (148, 66, 66), (22, 27, 27), (155, 73, 73), (122, 167, 167), (40, 22, 22), (39, 19, 19), (209, 70, 70), (192, 140, 140), (39, 131, 131), (125, 179, 179), (75, 164, 164), (229, 169, 169), (15, 31, 31), (51, 55, 55), (233, 220, 220), (159, 177, 177), (99, 44, 44), (35, 164, 164), (234, 171, 171), (105, 44, 44), (164, 209, 209), (151, 206, 206)]  
colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()


for y in range(-250, 250, 50):   
    for x in range(-250, 250, 50):
        tim.goto(x,y) 
        tim.dot(20, random.choice(color_list))


screen = Screen()
screen.exitonclick()
