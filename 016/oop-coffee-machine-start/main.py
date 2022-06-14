from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

clear = lambda: os.system('cls')

making_coffee = True
profit = 0

# create objects from classes
menu_item = MenuItem
menu = Menu
coffee_maker = CoffeeMaker
money_machine = MoneyMachine

while making_coffee:
    start_process = input("What would you like to drink? (espresso/latte/cappuccino)\n").lower()
    if start_process == "off":
        making_coffee = False
        clear
    elif start_process == "report":
        coffee_maker.report()