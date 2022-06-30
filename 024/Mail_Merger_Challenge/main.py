#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# my solution
# with open("024/Mail_Merger_Challenge/Input/Names/invited_names.txt", "r") as all_names:
#     all_names = all_names.readlines() # get the names and store in list
#     for name in all_names: # loop through all items (names) in list
#         stripped_name = name.strip()
#         with open("024/Mail_Merger_Challenge/Input/Letters/starting_letter.txt", "r") as start_letter:
#             letter_text = start_letter.read()
#             path = "024/Mail_Merger_Challenge/Output/ReadyToSend/" + stripped_name + ".txt" # create a letter for each name and saves in destined path
#             with open(path, "w") as letter:
#                 letter_text = letter_text.replace("[name]", stripped_name) # replace [name] with name from list
#                 letter.write(letter_text)
            

# Angelas Solution
PLACEHOLDER = "[name]"

with open("024/Mail_Merger_Challenge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("024/Mail_Merger_Challenge/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"024/Mail_Merger_Challenge/Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
    
        





