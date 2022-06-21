from turtle import Turtle, Screen, clear

tim = Turtle()
screen = Screen()

def move_fd():
    tim.fd(10)
def move_bk():
    tim.bk(10)
def move_rt():
    tim.rt(10)
def move_lt():
    tim.lt(10)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    # could use tim.reset() but any attributes assigned will be turned to default again, when screen is reset
def movements():
    w = screen.onkey(key="w", fun=move_fd)
    s = screen.onkey(key="s", fun=move_bk)
    a = screen.onkey(key="a", fun=move_lt)
    d = screen.onkey(key="d", fun=move_rt)
    c = screen.onkey(key="c", fun=clear_drawing)

screen.listen()
movements()
screen.exitonclick()
