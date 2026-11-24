import csv

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)

import json
with open("students.json", "w") as file:
    json.dump(row, file)
print("Data written successfully")
