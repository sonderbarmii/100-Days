from os import system
from secret_auction_art import logo
print(logo)
end_of_auction = False
list_of_bidders = {}
print("Welcome to the secret auction.")

def clear():
    _ = system("clear")

def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}.")

while not end_of_auction:
    name = input("What is your name? ")
    bid = int(input("How much do you want to bid? $"))
    list_of_bidders[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if more_bidders == "no":
        end_of_auction = True
        find_highest_bid(list_of_bidders)
    elif more_bidders == "yes":
        clear()       



