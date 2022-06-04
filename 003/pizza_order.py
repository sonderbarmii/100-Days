print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    pizza = 15
    pepperoni = 2
elif size == "M":
    pepperoni = 3
    pizza = 20
elif size == "L":
    pepperoni = 3
    pizza = 25
if add_pepperoni == "Y":
    final_price = pizza + pepperoni
if extra_cheese == "Y":
    final_price += 1
print(f"Your final bill is: {final_price}.")
