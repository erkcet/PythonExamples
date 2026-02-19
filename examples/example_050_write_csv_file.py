import csv

rows = [["name", "age"], ["Alice", 30], ["Bob", 25]]
with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("people.csv written")
