PATH = "CSVs\weather_data.csv"

import csv
import pandas

# with open(PATH) as data_files:
#     data = csv.reader(data_files)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#
#     print(temperatures)

data = pandas.read_csv(PATH)
data_dict = data.to_dict()
temp_list = data["temp"].to_list()
avg_temp = data["temp"].mean()
max_temp = data["temp"].max()
monday = data[data["day"] == "Monday"]
monday_temp_convert = (monday["temp"] * (9/5)) + 32
day_with_max_temp = data[data["temp"] == max_temp]

print(type(data))
print(data["temp"])
print(data_dict)
print(avg_temp)
print(max_temp)
print(monday)
print(monday_temp_convert)
print(day_with_max_temp)

