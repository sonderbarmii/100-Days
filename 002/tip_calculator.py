print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = int(input("How many people to split the bill? "))

new_tip = (int(tip) / 100) + 1
#print(new_tip)

amount = round((bill/people) * new_tip, 2)

print(f"Each person should pay: {amount}.")