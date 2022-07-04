import csv
import os
import numpy as np

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

date = []
money = []


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:
        date.append(row[0])
        cent = int(row[1])
        money.append(cent)


months = len(date)
total = sum(money)
i = 0
changes = []
while i < len(money) -1:
    current = money[i]
    future = money[i+1]
    difference = future - current
    changes.append(difference)
    i += 1

avg_change = np.mean(changes)
change_avg = round(avg_change, 2)
maximum_change = np.max(money)
max_index = money.index(maximum_change)
minimum_change = np.min(money)
min_index = money.index(minimum_change)

print(f"Financial Analysis")
print("----------------------------")
print(f"Total months: {months}")
print(f"Total: {total}")
print(f"Average Change: {change_avg}")
print(f"Greatest Increase in Profits: {date[max_index]} (${maximum_change})")
print(f"Greatest Decrease in Profits: {date[min_index]} (${minimum_change})")