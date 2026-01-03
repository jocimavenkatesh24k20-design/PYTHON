import csv

with open ("day-10/StudentsData.csv","w") as data:
    csv_writer = csv.writer(data)
    csv_writer.writerow(["Name","R.no","Dep"])
    csv_writer.writerow(["Jocima","20","cse"])
    csv_writer.writerow(["Ancy","21","ece"])
    csv_writer.writerow(["Princy","22","mech"])
