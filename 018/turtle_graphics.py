from turtle import *
import random
import turtle

tim = Turtle()
tim.shape("circle")
turtle.colormode(255)

# see notion for complete notes etc.

# for _ in range (15):
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()

# challenge draw square
# for _ in range(4):  # wir wollen 4 Seiten haben
#     tim.fd(100)
#     tim.rt(45)      # 45° Winkel


# challenge draw shapes 
# for i in range(3,11): # beginnend bei 3 Ecken (Dreieck), bis zu 11 Ecken
#     tim.color(random.randint(0,255), random.randint(0,255), random.randint(0,255)) # randomize colors
#     for _ in range(i):
#         tim.fd(100)
#         tim.rt(360/i)

# challenge random walk
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)   
    return (r,g,b)
# directions = [0, 90, 180, 270] # set the directions in degrees (0 - east, 90 - north, 180 - west, 270 - south)
# for _ in range(50):
#     tim.color(random_color())
#     tim.pensize(10)
#     tim.speed(10)
#     tim.fd(50)
#     tim.seth(random.choice(directions))

def draw_spiro(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.speed("fastest")
        tim.seth(tim.heading() + size_of_gap)

draw_spiro(10)









      










# we need to keep the below on the bottom on the file (exit!)
screen = Screen()
screen.exitonclick()