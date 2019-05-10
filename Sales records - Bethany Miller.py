import csv


with open("Sales Records.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    total = 0
    for row in reader:
        profit = row[13]
        category = row[2]
        print(profit)
        if category == "Fruits":
            profit = float(profit)
            total += profit
print(round(total, 2))

