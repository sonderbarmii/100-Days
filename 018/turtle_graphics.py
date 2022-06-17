from turtle import *
import random
import turtle

tim = Turtle()
tim.shape("circle")
colormode(255)

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


#direction
for _ in range(50):
    tim.color(random.randint(0,255), random.randint(0,255), random.randint(0,255)) # randomize colors
    tim.pensize(10)
    tim.speed(8)
    tim.fd(50)
    tim.right(random.randrange(0,360,90))










# we need to keep the below on the bottom on the file (exit!)
screen = Screen()
screen.exitonclick()