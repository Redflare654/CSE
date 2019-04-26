import csv


def valdidate(num: str):
    first_num = int(num[0])
    if first_num == 4:
        return True
    return False


with open("Book1.cvs", 'r') as old_csv:
    with open("myNewfile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
    print("processing...")

    for row in reader:
        old_number = row[0]
        first_num = int(old_number[0])
        if valdidate(old_number):
            writer.writerow(row)
print("ok")

