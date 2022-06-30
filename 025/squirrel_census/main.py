import pandas

data = pandas.read_csv("025/squirrel_census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Find out how many gray, cinnamon or black squirrels? (from Primary Fur Color)
#fur_color = data["Primary Fur Color"]
gray_squirrels = sum(data["Primary Fur Color"] == "Gray")
#print(sum(gray_squirrels))

cin_squirrels = sum(data["Primary Fur Color"] == "Cinnamon")
#print(sum(cin_squirrels))

black_squirrels = sum(data["Primary Fur Color"] == "Black")
#print(sum(black_squirrels))

data_dict = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cin_squirrels, black_squirrels],
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("025/squirrel_census/color_count.csv")