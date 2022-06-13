from higher_lower_art import logo, vs
from game_data import data
import random
import os
def clear():
    _ = system("clear")

def compare(guess, followers_a, followers_b):
  if followers_a > followers_b:
    return guess == "a"
  else:
    return guess == "b"
     
def print_person(person):
  return f"{person['name']}, a {person['description']}, from {person['follower_count']}"


# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"


def game():

  print(logo)
  
  score = 0
  game_over = False
  
  a = random.choice(data)
  b = random.choice(data)
  
  while not game_over:
    a = b
    b = random.choice(data)
    
    while a == b:
      b == random.choice(data)
  
    print(f"Compare A: {print_person(a)} ")
    print(vs)
    print(f"Against B: {print_person(b)} ")
    guess = input("Who has more followers? Type ‘A’ or ‘B: ").lower()
    followers_a = a['follower_count']
    followers_b = b['follower_count']
    check = compare(guess, followers_a, followers_b)

    clear()
    print(logo)
    
    if check:
      score += 1
      print(f"You\'re right. Your score: {score}.")
    else:
      game_over = True
      print(f"You\'re wrong. Your final score: {score}.")
            
  
game()
