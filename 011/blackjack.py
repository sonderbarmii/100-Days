import random
import os
from blackjack_art import logo

clear = lambda:os.system('cls')
start_game = input("Do you want to play a game of blackjack? Type 'y' or 'no'")
end_of_game = False
user_cards = []
computer_cards = []

def deal_card():
  """Returns a random card from the deck, see hint 4"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
def calculate_score(cards):  
  """Takes a list of cards as input and returns the score. If score > 21, remove the 11 and replace with 1. If score == 21, return 0."""
  if sum(cards) == 21 and len(cards) == 2: #represents the logic: a hand with 2 cards, one of them will be a 11 and the other a 10
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
for _ in range(2): 
  #_ because we do not need a variable but we want the loop to run twice
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Your cards: {user_cards}, current score: {user_score}.")
print(f"Computer's first card: {computer_cards[0]}.")
  
if user_score == 0 or computer_score == 0 or user_score > 21:
  end_of_game = True