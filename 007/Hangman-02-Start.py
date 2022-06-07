import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

position = display[0]

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)