import csv


with open("Sales Records.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        profit = row[13]
        category = row[2]
        print(profit)
        if category == "Fruits":
            print(profit, category)
