from secrets import choice
from typing_extensions import Self
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

clear = lambda: os.system('cls')

making_coffee = True

# create objects from classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while making_coffee:
    options = menu.get_items()
    start_process = input(f"What would you like to drink? {options}: ")
    if start_process == "off":
        making_coffee = False
    elif start_process == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(start_process)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


        