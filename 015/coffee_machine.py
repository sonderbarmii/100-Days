import os
from secrets import choice
from coffee_art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
clear = lambda: os.system('cls')

#print (logo)
making_coffee = True
profit = 0

def report():
    """prints current resources"""
    for level in resources:
        print(f"{level}: {resources[level]}")
        print(f"Money: {profit}")

def make_coffee(coffee_type, coffee_ingredients):
    """Reducing resources when processing coffee"""
    for item in coffee_ingredients:
      resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_type}. Enjoy!")

def processing_money(coffee_type_cost, amount_given):
    """Return True when the payment is accepted, False if money is insufficient."""
    if amount_given >= coffee_type_cost:
        change = round(amount_given - coffee_type_cost, 2)
        global profit
        profit += coffee_type_cost
        print(f"Here is ${change} in change. ")
        return True
    else:
        print("Sorry, that\'s not enough money. Here is your money back.")
        return False

def check_resources(coffee_type):
    """checking resources' levels. Returns True when order can be made, False when resources are not enough."""
    is_enough = True
    for item in coffee_type:
        if coffee_type[item] >= resources[item]:
            print("Sorry, there is not enough {item}.")
            is_enough =  False
    return is_enough
        
def calculate_income():
    """calculating the incoming payment"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? : ")) * 0.25
    dimes = int(input("How many dimes? : ")) * 0.1
    nickles = int(input("How many nickles? : ")) * 0.5
    pennies = int(input("How many pennies? : ")) * 0.01
    payment = float(round(quarters + dimes + nickles + pennies, 2))
    return payment


#process or action
while making_coffee:
    #1. Start the process, ask the user for coffee selection.
    start_process = input("What would you like to drink? (espresso/latte/cappuccino)\n").lower()
    print("Espresso: $ 1.50\nLatte: $2.5\nCappuccino: $3")
    #2. Turn off the Coffee Machine by entering "off" to the prompt.
    if start_process == "off":
        making_coffee = False
        clear
    #3. Print report.
    elif start_process == "report":
        report()
    else:
        drink = MENU[start_process]

        #4. Check resources sufficient?
        if check_resources(drink['ingredients']):
            # 5. Process coins.
            payment = calculate_income()
            if processing_money(drink['cost'], payment):
                make_coffee(start_process, drink['ingredients'])




