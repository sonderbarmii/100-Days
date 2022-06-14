# from turtle import Turtle, Screen

# timmy = Turtle() # create new object from blueprint
# print(timmy)
# timmy.shape("turtle") # call methods that are associated with the object
# timmy.color('green') # call methods that are associated with the object
# timmy.forward(100) # call methods that are associated with the object

# my_screen = Screen()
# print(my_screen.canvheight) # tap into object's attributes
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable() # create new object from class

# add data to columns
table.add_column("Pokémon name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table.align) # see alignment of table
# change alignment 'r' 'l' and 'c'
table.align = "l"

print(table)