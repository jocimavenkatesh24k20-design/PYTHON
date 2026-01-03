import csv

with open("day-10/StudentsData.csv", "r") as data:
    csv_reader = csv.reader(data)
    for row in csv_reader:
        print(row)