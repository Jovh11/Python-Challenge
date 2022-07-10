import csv
import os
import numpy as np

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

date = []
money = []

def mean_calc(array):
    mean = sum(array)/len(array)
    return mean

def min_max(array: list):
    new_array = array
    new_array.sort()
    min_val = new_array[0]
    max_val = new_array[-1]
    return min_val, max_val

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
unchanged = []
while i < len(money) -1:
    current = money[i]
    future = money[i+1]
    difference = future - current
    changes.append(difference)
    unchanged.append(difference)
    i += 1

print(changes)
avg_change = mean_calc(changes)
change_avg = round(avg_change, 2)
minimum_change, maximum_change = min_max(changes)
max_index = unchanged.index(maximum_change)
min_index = unchanged.index(minimum_change)

print(f"Financial Analysis")
print("----------------------------")
print(f"Total months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${change_avg}")
print(f"Greatest Increase in Profits: {date[max_index + 1]} (${maximum_change})")
print(f"Greatest Decrease in Profits: {date[min_index + 1]} (${minimum_change})")

output_file = os.path.join('PyBank.txt')

with open(output_file, 'w') as datafile:
    datafile.write(f"Financial Analysis")
    datafile.write('\n')
    datafile.write("----------------------------")
    datafile.write('\n')
    datafile.write(f"Total months: {months}")
    datafile.write('\n')
    datafile.write(f"Total: ${total}")
    datafile.write('\n')
    datafile.write(f"Average Change: ${change_avg}")
    datafile.write('\n')
    datafile.write(f"Greatest Increase in Profits: {date[max_index]} (${maximum_change})")
    datafile.write('\n')
    datafile.write(f"Greatest Decrease in Profits: {date[min_index]} (${minimum_change})")
