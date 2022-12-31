import csv

# with open("weather_data.csv") as file:
#     rows = csv.reader(file)
#     temperatures = []
#     for row in rows:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")

# print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day == "Monday"]
# faren = int(monday.temp * 9/5 + 32)
# print(faren)

squirrels = pandas.read_csv("Squirrels.csv")
gray = len(squirrels[squirrels.Fur == "Gray"])
red = len(squirrels[squirrels.Fur == "Cinnamon"])
black = len(squirrels[squirrels.Fur == "Black"])

dictionary = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count": [gray, red, black] 
}

pandas.DataFrame(dictionary).to_csv("squirrel_count.csv")