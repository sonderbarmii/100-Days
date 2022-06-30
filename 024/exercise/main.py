# reading a file
# with open("024/exercise/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# write to a file
with open("024/exercise/my_file.txt", mode="a") as file:
    file.write("\nHello")
