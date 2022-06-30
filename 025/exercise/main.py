# with open("025/exercise/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("025/exercise/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

from audioop import avg
import pandas

# data = pandas.read_csv("025/exercise/weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# find average
# print(round(sum(temp_list)/len(temp_list),2)) 
# print(data["temp"].mean())
# find maximum number
# print(data["temp"].max())

# get data from row
# print(data[data.day == "Monday"])
# get the row of data which had the highest temperature
# print(data[data.temp == data.temp.max()])

# access values from a row
# monday = data[data.day == "Monday"]
# convert celsius to fahrenheit
# monday_temp = int((monday.temp*9/5)+32)
# print(monday_temp)

# create dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("025/exercise/new_data.csv") # create new file