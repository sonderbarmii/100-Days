from os import system
from secret_auction_art import logo
print(logo)

end_of_auction = False
list_of_bidders = {}

def clear():
    _ = system("clear")

def add_new_bidder(add_name,  add_bid):
  list_of_bidders[add_name] = add_bid

print("Welcome to the secret auction.")

while end_of_auction:
    name = input("What is your name? ")
    bid = int(input("How much do you want to bid? "))
    add_new_bidder(add_name=name, add_bid=bid)
    more_bidders = input("Are there any other people who want to bid? Type 'yes' or 'no'. ").lower()
    if more_bidders == "no:"
        for i in list_of_bidders:
            placed_bid = list_of_bidders[i]
            
    clear()    


   

print(list_of_bidders)  

