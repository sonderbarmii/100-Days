print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names_temp = name1 + name2
names = names_temp.lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
l = names.count("l")
o = names.count("o")
v = names.count("v")
total_true = t + r + u + e 
total_love = l + o + v + e
total = int(str(total_true) + str(total_love))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")