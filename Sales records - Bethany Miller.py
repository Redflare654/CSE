import csv


with open("Sales Records.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    fruit_total = 0
    clothes_total = 0
    snacks_total = 0
    meat_total = 0
    cosmetics_total = 0
    personal_total = 0
    household_total = 0
    officesupplies_total = 0
    beverages_total = 0
    for row in reader:
        profit = row[13]
        category = row[2]
        if category == "Fruits":
            strawberry = float(profit)
            fruit_total += strawberry
        if category == "Clothes":
            pants = float(profit)
            clothes_total += pants
        if category == "Snacks":
            gummy = float(profit)
            snacks_total += gummy
        if category == "Meat":
            beef = float(profit)
            meat_total += beef
        if category == "Cosmetics":
            Cosmetics = float(profit)
            cosmetics_total += Cosmetics
        if category == "Personal Care":
            child_care = float(profit)
            personal_total += child_care
        if category == "Household":
            house = float(profit)
            household_total += house
        if category == "Office Supplies":
            staple = float(profit)
            officesupplies_total += staple
        if category == "Beverages":
            soda = float(profit)
            beverages_total += soda

print(round(fruit_total, 2))
print(round(clothes_total, 2))
print(round(snacks_total, 2))
print(round(cosmetics_total, 2))
print(round(personal_total, 2))
print(round(officesupplies_total, 2))
print(round(beverages_total, 2))