import random
from number_guessing_art import logo


remaining_tries = 0
end_of_game = False


def set_difficulty():
  ask_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if ask_difficulty == "easy":
    return remaining_tries + 10
  elif ask_difficulty == "hard":
    return remaining_tries + 5

def check_guess(user_guess, answer, remaining_tries):
  if user_guess > answer:
    print("Too high.")
    return remaining_tries - 1
  elif user_guess < answer:
    print("Too low.")
    return remaining_tries - 1
  else: 
    print(f"You got it! The answer was {answer}.")
           
def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I\'m thinking of a number between 1 and 100.")

  user_guess = 0
  answer = random.randint(1, 100)
  remaining_tries = set_difficulty()
  
  print(f"Pssst, the correct answer is {answer}.")


  while user_guess != answer:
    print(f"You have {remaining_tries} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    remaining_tries = check_guess(user_guess, answer, remaining_tries)
    if remaining_tries == 0:
      print("You ran out of guesses. You lose.")  
      return
    elif user_guess != answer:
        print("Guess again.")



play_game()

  
  