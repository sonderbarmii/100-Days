import pandas

data = pandas.read_csv("025/squirrel_census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# My Solution
gray_squirrels = sum(data["Primary Fur Color"] == "Gray")
cin_squirrels = sum(data["Primary Fur Color"] == "Cinnamon")
black_squirrels = sum(data["Primary Fur Color"] == "Black")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cin_squirrels, black_squirrels],
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("025/squirrel_census/color_count.csv")

# Angelas Solution
# data = pandas.read_csv("025/squirrel_census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrels = len(data[(data["Primary Fur Color"] == "Gray")])
# cin_squirrels = len(data[(data["Primary Fur Color"] == "Cinnamon")])
# black_squirrels = len(data[(data["Primary Fur Color"] == "Black")])

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels, cin_squirrels, black_squirrels],
# }
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("025/squirrel_census/color_count.csv")