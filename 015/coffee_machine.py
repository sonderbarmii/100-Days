import os
from menu import MENU, resources
from coffee_art import logo

clear = lambda: os.system('cls')

print (logo)
making_coffee = True
money = 2

def report():
    for level in resources:
        print(f"{level}: {resources[level]}")

#check amount of money
def processing_coffee(coffee_type):
    resources['water'] -= coffee_type['ingredients']['water']
    resources['milk'] -= coffee_type['ingredients']['milk']
    resources['coffee'] -= coffee_type['ingredients']['coffee']

    change = amount_given - coffee_type['cost']
    if amount_given == coffee_type['cost']:
        print("Thank you. Here is your {coffee_type}. Enjoy!")
    elif amount_given > coffee_type['cost']:
        print("Here is ${change} in change. ")
    else:
        print("Sorry, that\'s not enough money. Here is your money back.")
        

#Start and should reappear when action is completed.
def select_coffee():
    start_process = input("What would you like to drink? (espresso/latte/cappuccino)\n").lower()
    print("Espresso: $ .50\nLatte: $2.5\nCappuccino: $3")
    if start_process == "espresso":
        return MENU['espresso']
    elif start_process == "latte":
        return MENU['latte']
    elif start_process == "cappuccino":
        return MENU['cappuccino']



#check resources level
def check_resources(coffee_type):
    if resources['water'] < coffee_type['ingredients']['water']:
        return "Sorry, there is not enough water."
    elif resources['milk'] < coffee_type['ingredients']['milk']:
        return "Sorry, there is not enough milk."
    elif resources ['coffee'] < coffee_type['ingredients']['milk']:
        return "Sorry, there is not enough coffee."
        
#calculate the incoming payment
def calculate_income():
    quarters = int(input("How many quarters? : ")) * 0.25
    dimes = int(input("How many dimes? : ")) * 0.1
    nickles = int(input("How many nickles? : ")) * 0.5
    pennies = int(input("How many pennies? : ")) * 0.01
    paid = quarters + dimes + nickles + pennies
    return paid

print("Please insert coins.")

#deduct resources
resources select_coffee()


#process or action
while making_coffee:
    selection = select_coffee()
    if selection == "off":
        making_coffee = False
        clear
    elif selection == "report":
        report()
    