import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_name = random.randint(0, len(names)-1)
paying_person = names[random_name]
print(paying_person + " is going to buy the meal today!")