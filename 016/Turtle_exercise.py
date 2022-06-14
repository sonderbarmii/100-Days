from turtle import Turtle, Screen

timmy = Turtle() # create new object from blueprint
print(timmy)
timmy.shape("turtle") # call methods that are associated with he object
timmy.color('green') # call methods that are associated with he object
timmy.forward(100) # call methods that are associated with he object

my_screen = Screen()
print(my_screen.canvheight) # tap into object's attributes
my_screen.exitonclick()
