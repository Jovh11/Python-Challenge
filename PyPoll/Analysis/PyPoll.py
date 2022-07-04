import csv
import os
import numpy as np

candidate = []

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        candidate.append(row[2])

total_votes = len(candidate)
all_voted = np.unique(candidate)
new_voted = []
got_votes = []
votes_pct = []
for x in all_voted:
    value = str(x)
    new_voted.append(value)
new_voted.pop(0)
for x in new_voted:
    got_votes.append(candidate.count(x))
    percentage = round((candidate.count(x)/total_votes * 100), 3)
    votes_pct.append(percentage)
max_votes = np.max(got_votes)
finder = got_votes.index(max_votes)
winner = new_voted[finder]
print(f'Election Results')
print('-----------------------')
print(f'Total Votes: {total_votes}')
print('-----------------------')
i = 0
while i < len(new_voted):
    print(f'{new_voted[i]}: {votes_pct[i]}% ({got_votes[i]})')
    i += 1
print('-----------------------')
print(f'Winner: {winner}')
print('-----------------------')

output_file = os.path.join('PyPoll.txt')

with open(output_file, 'w') as datafile:
    datafile.write(f'Election Results')
    datafile.write('\n')
    datafile.write('-----------------------')
    datafile.write('\n')
    datafile.write(f'Total Votes: {total_votes}')
    datafile.write('\n')
    datafile.write('-----------------------')
    datafile.write('\n')
    i = 0
    while i < len(new_voted):
        datafile.write(f'{new_voted[i]}: {votes_pct[i]}% ({got_votes[i]})')
        datafile.write('\n')
        i += 1
    datafile.write('-----------------------')
    datafile.write('\n')
    datafile.write(f'Winner: {winner}')
    datafile.write('\n')
    datafile.write('-----------------------')
    datafile.write('\n')
