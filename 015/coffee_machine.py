import os
from menu import MENU
from coffee_art import logo
def clear():
    _ = system("clear")

print (logo)
making_coffee = True

#Start and should reappear when action is completed.
start_process = input("What would you like to drink? (espresso/latte/cappuccino)\n")

#option to turn the machine off
if start_process == "off":
    making_coffee = False
    clear()

