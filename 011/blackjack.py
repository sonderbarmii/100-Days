import random
import os
from blackjack_art import logo
clear = lambda:os.system('cls')

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
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose."
  elif user_score == computer_score:
    return "It's a draw."
  elif user_score == 0:
    return "Blackjack! You win!"
  elif computer_score == 0:
    return "Computer has a Blackjack! You lose."
  elif user_score > 21:
    return "Your score is over 21. You lose."
  elif computer_score > 21:
    return "Computer is over 21. You win!"
  elif user_score > computer_score:
    return "You win."
  else:
    return "You lose."
def play_game():
  print(logo)
  
  end_of_game = False
  user_cards = []
  computer_cards = []

  for _ in range(2): 
    #_ because we do not need a variable but we want the loop to run twice
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not end_of_game:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}.")
    print(f"Computer's first card: {computer_cards[0]}.")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      end_of_game = True
    else:
      should_continue = input("Do you want to draw a card? Type 'y' or 'n' to pass: ")
      if should_continue == "y":
        user_cards.append(deal_card())
      else:
        end_of_game = True
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    
  print(f"Your final hand is {user_cards},  final score: {user_score}.")
  print(f"Computer's final hand is {computer_cards}, final score: {computer_score}.")
  print(compare(user_score, computer_score))
    
while input("Do you want to play a game of blackjack? Type 'y' or 'no'") == "y":
  clear()
  play_game()

