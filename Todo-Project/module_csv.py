import csv

with open("weather.csv","r")as file:
    data=list(csv.reader(file))

print(data)